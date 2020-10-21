from io import BytesIO

import qrcode
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import gettext_lazy as _

from census.consts import REGION_CHOICES, SERIAL_CHOICES, ROLE_CHOICES
from census.singleton_model import SingletonModel


class Employee(models.Model):
    last_name = models.CharField(_('фамилиясы'), max_length=45)
    first_name = models.CharField(_('аты'), max_length=45)
    patronymic = models.CharField(_('атасынын аты'), max_length=45, null=True, blank=True)
    birth_day = models.DateField(_('туулган күн'))
    address = models.CharField(_('дарек'), max_length=255)

    serial = models.CharField(
        _('паспорт сериасы'),
        max_length=2,
        choices=SERIAL_CHOICES,
        default='ID'
    )
    passport_number = models.CharField(
        _('паспорт номери'),
        max_length=7,
        unique=True
    )
    PIN = models.CharField(_('ПИН'), max_length=14, unique=True)
    photo = models.ImageField(_('сүрөт'), upload_to='employee/photos')
    role = models.PositiveSmallIntegerField(_('ролу'), choices=ROLE_CHOICES, default=1)
    territory = models.ForeignKey(
        'census.Territory',
        on_delete=models.SET_NULL,
        verbose_name=_('aймак'),
        null=True, blank=False)
    agreement = models.CharField(_('келишим'), max_length=6, blank=True, null=True)
    qr_code = models.ImageField(_('QR код'), upload_to='employee/qr-codes', blank=True, null=True)

    class Meta:
        verbose_name = _("Кызматкер")
        verbose_name_plural = _('Кызматкерлер')

    @property
    def role_str(self):
        return dict(ROLE_CHOICES).get(self.role)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name[0]}.'

    def generate_qr_code(self):
        QRCode = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=2
        )
        QRCode.add_data(self.full_name)
        QRCode.make(fit=True)

        img = QRCode.make_image()
        buffer = BytesIO()
        img.save(buffer)
        filename = f'qr_code-{self.id}.png'
        file = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.tell(), None
        )

        self.qr_code.save(filename, file, save=False)


class District(models.Model):
    region = models.CharField(_('область'), max_length=2, choices=REGION_CHOICES)
    name = models.CharField(_('аты'), max_length=55)
    gov_admin = models.CharField(_('мам админстрация башчы (ААТ)'), max_length=255)
    stat_admin = models.CharField(_('статистика башчы (ААТ)'), max_length=255)
    center = models.CharField(_('райондун борбору'), max_length=255)
    stat_address = models.CharField(_('статистика бөлүмдүн дареги'), max_length=255)
    counter = models.CharField(_('келишимдин саны'), max_length=6, default='000001')
    number = models.CharField(_('райондун ID -си'), max_length=2, null=True, blank=True)

    class Meta:
        verbose_name = _("Район")
        verbose_name_plural = _('Райондор')
        ordering = ['region']


class Territory(models.Model):
    name = models.CharField(_('аты'), max_length=90)
    code = models.CharField(_('код'), max_length=14, unique=True)
    district = models.ForeignKey(District, models.CASCADE, verbose_name=_('район'))

    class Meta:
        verbose_name = _('Аймак')
        verbose_name_plural = _('Аймактар')
        ordering = ['code']

    def __str__(self):
        return f'{self.name}'


class SiteSettings(SingletonModel):
    role = models.PositiveSmallIntegerField(_('ролу'), choices=ROLE_CHOICES, default=1)

    class Meta:
        verbose_name = 'Конфигурация'
        verbose_name_plural = 'Конфигурациялар'

    def __str__(self):
        return f'{_("Конфигурациялар")}'
