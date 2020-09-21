from django.shortcuts import render
from django.views.generic import CreateView, ListView

from census.forms import EmployeeCreateForm
from census.models import Employee


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'index.html'
    form_class = EmployeeCreateForm


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees.html'
