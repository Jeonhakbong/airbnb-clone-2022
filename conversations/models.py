from django.db import models
from core import models as core_models

# Create your models here.
class Conversation(core_models.TimeStampedModel):

    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        all_users = []
        for user in self.participants.all():
            all_users.append(user.username)
        return ", ".join(all_users)

    def count_msgs(self):
        return self.messages.count()  # can get count from messages(messages set)

    def count_participants(self):
        return self.participants.count()


class Message(core_models.TimeStampedModel):

    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):

        return f"{self.user} says: {self.message}"
