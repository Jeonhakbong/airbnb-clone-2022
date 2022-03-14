from ast import arg
from curses import savetty
from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as users_models

# Create your models here.
class AbstractItem(core_models.TimeStampedModel):

    """AbstractItem"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    # Relationship
    # users_models.User can also be "users.User"
    host = models.ForeignKey(
        users_models.User, related_name="rooms", on_delete=models.CASCADE
    )  # many to one
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", null=True, on_delete=models.SET_NULL
    )
    amenities = models.ManyToManyField(
        Amenity, related_name="rooms", blank=True
    )  # many to many
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)  # real save() method

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()  # get review_set
        total_rating = 0
        for review in all_reviews:
            # print(review.rating_average())
            total_rating += review.rating_average()
        return total_rating / len(all_reviews)


class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="rooms_photos")
    room = models.ForeignKey(Room, related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
