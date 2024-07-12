# Import AppConfig class from django.apps module
from django.apps import AppConfig


class HtmxConfig(AppConfig):
    """
    Configuration class for the htmx application.
    This class sets the default auto field and application name.
    """
    
    # Define default auto field type for primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the application
    name = 'htmx'
