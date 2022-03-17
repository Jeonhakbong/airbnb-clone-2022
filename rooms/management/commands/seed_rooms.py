import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command create rooms."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="Enter the number how many you want"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 8),
                "price": lambda x: random.randint(1, 1000),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 2),
            },
        )
        created_pks = (
            seeder.execute()
        )  # execute() return the list of pk(==id), so we can get the list.
        # print(created_pks.values())
        created_pks_list = flatten(list(created_pks.values()))
        # print(created_pks_list)

        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in created_pks_list:
            room = room_models.Room.objects.get(pk=pk)

            # import photo. : foreign key
            for i in range(3, random.randint(5, 17)):  # create photo 3 ~ 10~17.
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"rooms_photos/{random.randint(1, 32)}.webp",
                    room=room,
                )

            # import amenities, facilities and house rule. : many-to-many field
            for a in amenities:
                rand_num = random.randint(0, 15)
                if rand_num % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                rand_num = random.randint(0, 15)
                if rand_num % 2 == 0:
                    room.facilities.add(f)

            for r in rules:
                rand_num = random.randint(0, 15)
                if rand_num % 2 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms crearted!"))
