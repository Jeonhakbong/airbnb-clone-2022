import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command create reservations."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="Enter the number how many you want"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status0": lambda x: random.choice(
                    ["pending", "confirmed", "canceled"]
                ),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(1, 25)),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} reservations crearted!"))
