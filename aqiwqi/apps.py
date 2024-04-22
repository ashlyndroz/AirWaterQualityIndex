# myapp/apps.py
from django.apps import AppConfig
from .mqtt_connector import start_mqtt_client

class AqiwqiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aqiwqi'


