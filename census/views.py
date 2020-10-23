from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView

from census.filters import EmployeeFilter
from census.forms import EmployeeCreateForm, EmployeeUpdateForm
from census.models import Employee


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'index.html'
    form_class = EmployeeCreateForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


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
    paginate_by = 20
    model = Employee
    template_name = 'employees.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_superuser:
            return queryset

        filtered = queryset.filter(territory__district=self.request.user.profile.district)
        return filtered


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee.html'


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = 'update.html'
    form_class = EmployeeUpdateForm


class AgreementDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'agreement.html'


class PrintConfirmView(View):

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        user = request.user

        if user.is_authenticated and user.is_superuser:
            print(request.user.get_username())
        else:
            print("Foo")
        data = {
            'okay': True
        }
        return JsonResponse(data)
