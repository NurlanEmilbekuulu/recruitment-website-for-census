from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView

from census.filters import EmployeeFilter
from census.forms import EmployeeCreateForm, EmployeeUpdateForm
from census.models import Employee


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'index.html'
    form_class = EmployeeCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class FiltersetFormView(TemplateView):
    filterset: object
    filterset_class = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        self.filterset = self.filterset_class()
        context['form'] = self.filterset.form
        return context


class EmployeeListView(LoginRequiredMixin, FiltersetFormView):
    filterset_class = EmployeeFilter
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
