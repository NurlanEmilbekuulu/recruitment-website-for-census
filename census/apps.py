from django.apps import AppConfig


class CensusConfig(AppConfig):
    name = 'census'

    def ready(self):
        import census.signals
