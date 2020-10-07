import random
import secrets
import string

from django.contrib.auth.models import User


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def get_secure_random_string(length):
    secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(length)))
    return secure_str


def create_users(district):
    admin_username = get_random_alphanumeric_string(8)
    admin_password = get_secure_random_string(8)

    mod_username = get_random_alphanumeric_string(8)
    mod_password = get_secure_random_string(8)

    admin = User.objects.create_user(
        username=admin_username,
        password=admin_password
    )

    moderator = User.objects.create_user(
        username=mod_username,
        password=mod_password
    )

    admin.profile.raw_password = admin_password
    admin.profile.district = district
    admin.profile.role = 1

    moderator.profile.raw_password = mod_password
    moderator.profile.district = district
    moderator.profile.role = 2

    admin.save()
    moderator.save()

    return True
