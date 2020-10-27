from django import forms

from census.models import Employee, Territory


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['agreement', 'qr_code']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if user.is_superuser:
            territory_queryset = Territory.objects.all()
        else:
            territory_queryset = Territory.objects.filter(district=user.profile.district)

        self.fields['territory'].queryset = territory_queryset


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['agreement', 'qr_code', 'photo']


class PhotoCropForm(forms.Form):
    x1 = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'x1'}), required=False)
    y1 = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'y1'}), required=False)
    x2 = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'x2'}), required=False)
    y2 = forms.CharField(widget=forms.HiddenInput(attrs={'id': 'y2'}), required=False)
