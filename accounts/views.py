from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic.base import View

from accounts.utils import create_users
from census.models import District


class UAGView(View):

    @staticmethod
    def get(request):
        districts = District.objects.all()

        for district in districts:
            create_users(district)

        messages.success(request, 'Profile updated successfully')
        return redirect(reverse_lazy('admin:accounts_profile_changelist'))

