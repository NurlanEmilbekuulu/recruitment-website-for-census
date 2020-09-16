from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.views.generic import TemplateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', TemplateView.as_view(template_name="base.html"))
# ]

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base.html"))
)
