from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models

# from rooms.models import Amenity   # or can use this code.


class Command(BaseCommand):

    help = "This command create amenities."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="Enter the number how many you want"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        seeder.add_entity(
            user_models.User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} user crearted!"))
