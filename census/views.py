from io import BytesIO

from PIL import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView

from census.filters import EmployeeFilter
from census.forms import EmployeeCreateForm, EmployeeUpdateForm, PhotoCropForm
from census.models import Employee
from census.utils import rotate_image


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'index.html'
    form_class = EmployeeCreateForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_crop_form = PhotoCropForm(prefix='crop')
        context['photo_crop_form'] = photo_crop_form
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        crop = PhotoCropForm(self.request.POST, prefix='crop')
        if crop.is_valid():
            buffer = BytesIO()
            x1 = int(crop.cleaned_data['x1'])
            y1 = int(crop.cleaned_data['y1'])
            x2 = int(crop.cleaned_data['x2'])
            y2 = int(crop.cleaned_data['y2'])
            image = form.cleaned_data['photo']
            img = Image.open(image)
            profile_img = img.crop((x1, y1, x2, y2))
            profile_img.save(buffer, format='JPEG')
            filename = f'profile.jpg'
            file = InMemoryUploadedFile(
                buffer, None, filename, 'image/jpeg', buffer.tell(), None
            )
            instance.photo = file
            instance.save()

        return super().form_valid(form)


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
    def get(self, request, pk):
        user = request.user
        employee = Employee.objects.get(pk=pk)

        if user.is_authenticated and user.is_superuser:
            print(request.user.get_username())
            employee.generate_qr_code()
        else:
            print("Foo")
        data = {
            'okay': True
        }
        return JsonResponse(data)
