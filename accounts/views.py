from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import View

from accounts.utils import get_random_alphanumeric_string, get_secure_random_string


class UAGView(View):

    def get(self, request):
        username = get_random_alphanumeric_string(8)
        password = get_secure_random_string(8)
        user = User.objects.create_user(
            username=username,
            password=password
        )

        user.profile.raw_password = password

        user.save()
        return redirect(reverse_lazy('admin:accounts_profile_changelist'))
