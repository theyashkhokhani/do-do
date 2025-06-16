from django.apps import AppConfig

class ThoughtsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'thoughts'

    def ready(self):
        import thoughts.signals