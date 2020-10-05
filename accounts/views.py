from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import View


class UAGView(View):

    def get(self, request):
        print("Hello World")
        return redirect(reverse_lazy('admin:accounts_profile_changelist'))
