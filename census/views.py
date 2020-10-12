from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from census.filters import EmployeeFilter
from census.forms import EmployeeCreateForm, EmployeeUpdateForm
from census.models import Employee


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'index.html'
    form_class = EmployeeCreateForm


class FilteredListView(ListView):
    filterset: object
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class EmployeeListView(LoginRequiredMixin, FilteredListView):
    filterset_class = EmployeeFilter
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
