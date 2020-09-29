from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from census.forms import EmployeeCreateForm, EmployeeUpdateForm
from census.models import Employee


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'index.html'
    form_class = EmployeeCreateForm


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee.html'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'update.html'
    form_class = EmployeeUpdateForm


class AgreementDetailView(DetailView):
    model = Employee
    template_name = 'agreement.html'
