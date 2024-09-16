from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Import the signals file here
