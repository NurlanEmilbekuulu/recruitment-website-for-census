from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import LanguageView

urlpatterns = [
    path('api/', include('census.api.urls')),
    path('lang/<str:lang>', LanguageView.as_view(), name='lang')
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('census.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
