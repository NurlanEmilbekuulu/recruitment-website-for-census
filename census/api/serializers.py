from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.utils import translation as t
from census.models import Employee


class EmployeeSerializer(ModelSerializer):
    update_url_suffix = SerializerMethodField()
    agreement_url_suffix = SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    # noinspection PyMethodMayBeStatic
    def get_update_url_suffix(self, obj):
        request_obj = self.context['request']
        return f'/employee/{obj.id}/change'

    # noinspection PyMethodMayBeStatic
    def get_agreement_url_suffix(self, obj):
        request_obj = self.context['request']
        return f'/employee/{obj.id}/agreement'
