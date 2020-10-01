from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.consts import ROLE_CHOICES


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(_('ролу'), choices=ROLE_CHOICES, default=1)
    district = models.OneToOneField('census.District', on_delete=models.PROTECT, verbose_name=_('район'), null=True)
    raw_password = models.CharField(_('сырсөз'), max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профилдер'
