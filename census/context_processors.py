from django.conf import settings

from census.models import SiteSettings


def api_endpoint(request):
    return {'API_ENDPOINT': settings.API_ENDPOINT}


def load_settings(request):
    return {'site_settings': SiteSettings.load()}
