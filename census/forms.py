from django import forms

from census.models import Employee


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['agreement', 'qr_code']


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['agreement', 'qr_code']
