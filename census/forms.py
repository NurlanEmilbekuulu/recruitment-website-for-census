from django import forms

from census.models import Employee


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
