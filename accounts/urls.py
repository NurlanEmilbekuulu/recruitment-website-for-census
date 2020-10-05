from django.urls import path

from accounts.views import UAGView

urlpatterns = [
    path('generate/', UAGView.as_view(), name='auto-user-generation'),
]
