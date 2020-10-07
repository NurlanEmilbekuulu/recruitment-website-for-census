import random
import secrets
import string

from django.contrib.auth.models import User

from accounts.models import Profile


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def get_secure_random_string(length):
    secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(length)))
    return secure_str


def is_users_exist_by_district(district):
    users = Profile.objects.filter(district=district)
    return len(users) > 0, len(users)


def create_user(district, role=1):
    username = get_random_alphanumeric_string(8)
    password = get_secure_random_string(8)

    user = User.objects.create_user(
        username=username,
        password=password
    )

    user.profile.raw_password = password
    user.profile.district = district
    user.profile.role = role

    user.save()


def create_users(district):
    control, length = is_users_exist_by_district(district)
    if control and length == 1:
        user = User.objects.get(profile__district=district)
        if not user.is_superuser:
            if user.profile.role == 1:
                create_user(district, role=2)
            else:
                create_user(district, role=1)
            return True
    if not control:
        create_user(district, role=1)
        create_user(district, role=2)
        return True

    return False
