import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command create lists."

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
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created_pks = seeder.execute()
        created_pks_list = flatten(list(created_pks.values()))

        for pk in created_pks_list:
            my_list = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 3) : random.randint(3, 6)]
            my_list.rooms.add(
                *to_add
            )  # to_add is list. we need to add elements of to_add

            # for r in rooms:
            #     rand_num = random.randint(0, 15)
            #     if rand_num % 2 == 0:
            #         my_list.room.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} lists crearted!"))
