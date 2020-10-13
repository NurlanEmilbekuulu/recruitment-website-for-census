from django.db import models
from django.utils.translation import gettext_lazy as _

from census.consts import REGION_CHOICES, SERIAL_CHOICES, ROLE_CHOICES
from census.singleton_model import SingletonModel


class Employee(models.Model):
    last_name = models.CharField(_('last name'), max_length=45)
    first_name = models.CharField(_('first name'), max_length=45)
    patronymic = models.CharField(_('patronymic'), max_length=45, null=True, blank=True)
    birth_day = models.DateField(_('birth day'))
    address = models.CharField(_('address'), max_length=255)

    serial = models.CharField(
        _('serial'),
        max_length=2,
        choices=SERIAL_CHOICES,
        default='ID'
    )
    passport_number = models.CharField(
        _('passport number'),
        max_length=7,
        unique=True
    )
    PIN = models.CharField(_('PIN'), max_length=14, unique=True)
    photo = models.ImageField(_('photo'), upload_to='employee/photos')
    role = models.PositiveSmallIntegerField(_('role'), choices=ROLE_CHOICES, default=1)
    agreement = models.CharField(_('келишим'), max_length=6, blank=True, null=True)
    qr_code = models.ImageField(_('QR код'), upload_to='users/qr-codes', blank=True, null=True)

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _('Employees')

    @property
    def role_str(self):
        return dict(ROLE_CHOICES).get(self.role)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name[0]}.'


class District(models.Model):
    region = models.CharField(_('region'), max_length=2, choices=REGION_CHOICES)
    name = models.CharField(_('name'), max_length=55)
    gov_admin = models.CharField(_('Мам админстрация башчы (ААТ)'), max_length=255)
    stat_admin = models.CharField(_('Статистика башчы (ААТ)'), max_length=255)
    center = models.CharField(_('center of the district'), max_length=255)
    stat_address = models.CharField(_('stat address'), max_length=255)
    counter = models.CharField(max_length=6, default='000001')
    number = models.CharField(_('id of the district'), max_length=2, null=True, blank=True)

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _('Districts')
        ordering = ['region']


class Territory(models.Model):
    name = models.CharField(_('name'), max_length=90)
    code = models.CharField(_('code'), max_length=14, unique=True)
    district = models.ForeignKey(District, models.CASCADE, verbose_name=_('district'))

    class Meta:
        verbose_name = _('Territory')
        verbose_name_plural = _('Territories')
        ordering = ['code']

    def __str__(self):
        return f'{self.name}'


class SiteSettings(SingletonModel):
    role = models.PositiveSmallIntegerField(_('role'), choices=ROLE_CHOICES, default=1)

    class Meta:
        verbose_name = 'Конфигурация'
        verbose_name_plural = 'Конфигурациялар'

    def __str__(self):
        return f'{_("Конфигурациялар")}'
