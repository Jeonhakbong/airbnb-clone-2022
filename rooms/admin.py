from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    # use room_set(rooms, foreign key)
    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    inlines = (PhotoInline,)

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

    raw_id_fields = ("host",)

    # we can access to foreign key's attributes
    search_fields = ["city", "^host__username"]

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

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        # print(dir(obj.file)) # check it out

        # f'<img src="{obj.file.url}" />'
        # We can't use this html tag in django beacause of 'security'.
        # We need to import mark_safe()
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
