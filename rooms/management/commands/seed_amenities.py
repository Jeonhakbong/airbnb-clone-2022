from django.core.management.base import BaseCommand
from rooms import models as room_models

# from rooms.models import Amenity   # or can use this code.


class Command(BaseCommand):

    help = "This command create amenities."

    # def add_arguments(self, parser):

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Heating",
            "Washer",
            "Wifi",
            "Indoor fireplace",
            "Iron",
            "Laptop friendly workspace",
            "Crib",
            "Self check-in",
            "Carbon monoxide detector",
            "Shampoo",
            "Air conditioning",
            "Dryer",
            "Breakfast",
            "Hangers",
            "Hair dryer",
            "TV",
            "High chair",
            "Smoke detector",
            "Private bathroom",
        ]

        for amenity in amenities:
            room_models.Amenity.objects.create(name=amenity)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} amenities created!"))
