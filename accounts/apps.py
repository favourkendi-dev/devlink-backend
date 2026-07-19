from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # This runs when the accounts app is ready We import signals.py here so Django actually registers our create_profile function to listen for the post_save event
    
    def ready(self):
        import accounts.signals