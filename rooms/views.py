from cgi import print_exception
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models

# we don't need to programming like return render. Just configurate it with django.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    context_object_name = "rooms"  # object_list to rooms.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


def search(request):
    DEFAULT_VALUE = 0

    city = str.capitalize(request.GET.get("city", "Anywhere"))
    sel_country = request.GET.get("country", "KR")
    sel_room_type = int(request.GET.get("room_type", DEFAULT_VALUE))
    price = int(request.GET.get("price", DEFAULT_VALUE))
    guests = int(request.GET.get("guests", DEFAULT_VALUE))
    bedrooms = int(request.GET.get("bedrooms", DEFAULT_VALUE))
    beds = int(request.GET.get("beds", DEFAULT_VALUE))
    baths = int(request.GET.get("baths", DEFAULT_VALUE))
    instant = bool(request.GET.get("instant", False))
    superhost = bool(request.GET.get("superhost", False))
    sel_amenities = request.GET.getlist("amenities")
    sel_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "sel_country": sel_country,
        "sel_room_type": sel_room_type,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "instant": instant,
        "superhost": superhost,
        "sel_amenities": sel_amenities,
        "sel_facilities": sel_facilities,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    # use field lookups : how you specify the meat of an SQL WHERE clause.
    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    if sel_room_type != DEFAULT_VALUE:
        filter_args["room_type__pk__exact"] = sel_room_type

    if price != DEFAULT_VALUE:
        filter_args["price__lte"] = price

    if guests != DEFAULT_VALUE:
        filter_args["guests__gte"] = guests

    if bedrooms != DEFAULT_VALUE:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != DEFAULT_VALUE:
        filter_args["beds__gte"] = beds

    if baths != DEFAULT_VALUE:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        # superhost is not in room models. so we use foreign key.
        filter_args["host__superhost"] = True

    if len(sel_amenities) > 0:
        for sel_amenity in sel_amenities:
            filter_args["amenities__pk"] = int(sel_amenity)

    if len(sel_facilities) > 0:
        for sel_facility in sel_facilities:
            filter_args["facilities__pk"] = int(sel_facility)

    filter_args["country"] = sel_country
    print(filter_args)

    rooms = models.Room.objects.filter(**filter_args)
    print(rooms)

    return render(
        request,
        "rooms/search.html",
        context={
            **form,
            **choices,
            "rooms": rooms,
        },
    )
