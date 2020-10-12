from rest_framework.viewsets import ModelViewSet

from census.api.serializers import EmployeeSerializer
from census.models import Employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['first_name', 'last_name']
