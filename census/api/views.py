from rest_framework.viewsets import ModelViewSet

from census.api.serializers import EmployeeSerializer
from census.filters import EmployeeFilter
from census.models import Employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter
