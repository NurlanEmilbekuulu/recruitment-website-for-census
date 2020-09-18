from django.urls import path

from census.views import EmployeeCreateView

urlpatterns = [
    path('', EmployeeCreateView.as_view())
]
