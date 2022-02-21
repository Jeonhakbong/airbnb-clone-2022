from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = ("^name",)  # ^ : start with

    list_filter = ("user",)

    filter_horizontal = ("rooms",)
