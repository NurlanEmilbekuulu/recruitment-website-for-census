import django_filters

from census.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'first_name': ['icontains', ],
            'last_name': ['icontains', ],
            'PIN': ['exact', ],
            'role': ['exact', ],
        }
