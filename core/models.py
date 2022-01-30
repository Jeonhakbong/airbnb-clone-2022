from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # We dont want TimeStampedModel to be registered on database
    class Meta:  # put extra information
        abstract = True  # make this class to 'abstract class'
