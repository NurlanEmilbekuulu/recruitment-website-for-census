from django.urls import path

from census.views import EmployeeCreateView, EmployeeListView, EmployeeDetailView, EmployeeUpdateView

urlpatterns = [
    path('', EmployeeCreateView.as_view()),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee'),
    path('employee/<int:pk>/change/', EmployeeUpdateView.as_view(), name='update'),
]
