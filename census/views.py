from django.shortcuts import render
from django.views.generic import CreateView

from census.forms import EmployeeCreateForm
from census.models import Employee


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'index.html'
    form_class = EmployeeCreateForm
