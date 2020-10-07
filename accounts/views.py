from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import View

from accounts.utils import create_users
from census.models import District


class UAGView(View):

    def get(self, request):

        districts = District.objects.all()

        for district in districts:
            create_users(district)

        messages.success(request, 'Profile updated successfully')
        return redirect(reverse_lazy('admin:accounts_profile_changelist'))
