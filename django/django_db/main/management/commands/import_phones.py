from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'USAGE ./python manage.py import_phones'

    def handle(self, *args: Any, **options: Any) -> str | None:
        import this