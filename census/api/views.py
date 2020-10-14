from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from census.api.serializers import EmployeeSerializer
from census.filters import EmployeeFilter
from census.models import Employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter

    @action(detail=True, methods=['get'])
    def generate_qr_code(self, request, pk=None):
        employee = self.get_object()
        if not employee.qr_code:
            employee.generate_qr_code()
            employee.save()
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
