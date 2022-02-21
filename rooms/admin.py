from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    # use room_set(foreign key)
    def used_by(self, obj):
        return obj.rooms.count()


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
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "city",
        "country",
    )

    # we can access to foreign key's attributes
    search_fields = ["city", "host__username"]

    # filter for many-to-many in FIeld Set
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    # self is class, obj(object) is current row on admin panel.
    def count_amenities(self, obj):
        return obj.amenities.count()

    # count_amenities.short_description = "Num of Amenities"

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
