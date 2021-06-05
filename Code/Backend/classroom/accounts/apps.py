from django.apps import AppConfig
from django.apps import classes


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
