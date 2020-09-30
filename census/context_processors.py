from django.conf import settings


def api_endpoint(request):
    return {'API_ENDPOINT': settings.API_ENDPOINT}
