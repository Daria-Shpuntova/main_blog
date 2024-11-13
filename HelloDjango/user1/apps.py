from django.apps import AppConfig


class User1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user1'

    def ready(self):
        import user1.signals