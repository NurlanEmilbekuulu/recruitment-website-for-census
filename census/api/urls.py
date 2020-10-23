from django.urls import path, include
from rest_framework import routers
from census.api.views import EmployeeViewSet, BadgePrintConfirmView

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet, 'Employee')

urlpatterns = [
    path('', include(router.urls)),
    path('current/', BadgePrintConfirmView.as_view())
]
