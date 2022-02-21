from optparse import check_builtin
from django.db import models
from django.utils import timezone  # django knows that our server is on Asia/Seoul
from core import models as core_models

# Create your models here.
class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    # reservation status choices
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        choices=STATUS_CHOICES, max_length=10, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()

    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    # booker = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # guests = models.IntegerField()
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()  # get date of now
        if self.status == self.STATUS_CONFIRMED:
            return now > self.check_in and now < self.check_out
        else:
            return False

    in_progress.boolean = True  # can get boolean icon

    def is_finished(self):
        now = timezone.now().date()

        if self.status == self.STATUS_CONFIRMED:
            return now > self.check_out
        else:
            return False

    is_finished.boolean = True
