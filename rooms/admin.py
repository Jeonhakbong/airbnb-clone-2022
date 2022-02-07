from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "host",
                    "country",
                    "city",
                    "address",
                )
            },
        ),
        (
            "Book Info",
            {
                "fields": (
                    "price",
                    "guests",
                    "check_in",
                    "check_out",
                    "instant_book",
                )
            },
        ),
        (
            "Spaces Info",
            {
                "fields": (
                    "room_type",
                    "beds",
                    "bedrooms",
                    "baths",
                    "amenities",
                    "facilities",
                    "house_rules",
                )
            },
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = (
        "city",
        "country",
    )

    # we can access to foreign key's attributes
    search_fields = ["city", "host__username"]

    # filter for many-to-many
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    # self is class, obj(object) is current row on admin panel.
    def count_amenities(self, obj):
        print(obj.amenities.all())

        return

    count_amenities.short_description = "Num of Amenities"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
