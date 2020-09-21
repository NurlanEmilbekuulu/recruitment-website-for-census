from django.urls import path

from census.views import EmployeeCreateView, EmployeeListView

urlpatterns = [
    path('', EmployeeCreateView.as_view()),
    path('employees/', EmployeeListView.as_view(), name='employees'),
]
