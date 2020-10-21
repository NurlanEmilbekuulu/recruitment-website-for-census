from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField, DateField
from census.models import Employee


class EmployeeSerializer(ModelSerializer):
    update_url_suffix = SerializerMethodField()
    agreement_url_suffix = SerializerMethodField()
    full_name = ReadOnlyField()
    role_str = ReadOnlyField()
    birth_day = DateField(format='%d.%m.%Y')

    class Meta:
        model = Employee
        fields = '__all__'

    # noinspection PyMethodMayBeStatic
    def get_update_url_suffix(self, obj):
        return f'/employee/{obj.id}/change'

    # noinspection PyMethodMayBeStatic
    def get_agreement_url_suffix(self, obj):
        return f'/employee/{obj.id}/agreement'
