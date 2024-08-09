import csv
import datetime
from typing import Any
from django.core.management.base import BaseCommand
from main.models import Phones

class Command(BaseCommand):
    help = 'USAGE ./python manage.py import_phones'

    def handle(self, *args: Any, **options: Any) -> str | None:
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            #datetime.date.today() = 2024-08-09
            print(phones)
            for phone in phones:
                # Добавьте сохранение модели
                p = Phones.objects.create(
                    id=phone["id"],
                    name=phone["name"],
                    image=phone["image"],
                    price=phone["price"],
                    release_date=phone["release_date"],
                    lte_exists=phone["lte_exists"],
                    slug=phone["name"]
                    )
        
        self.stdout.write(
                self.style.SUCCESS('Well done! The data were written successfully! "%s"' % p)
            )