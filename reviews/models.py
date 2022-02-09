from django.db import models
from core import models as core_models
from users import models as users_models
from rooms import models as rooms_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    cleanliness = models.IntegerField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    user = models.ForeignKey(
        users_models.User, related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        rooms_models.Room, related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"  # use __str__ better (self.room)
