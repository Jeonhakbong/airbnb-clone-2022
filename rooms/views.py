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
    city = str.capitalize(request.GET.get("city"))
    sel_country = request.GET.get("country")
    sel_room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant", False)
    superhost = request.GET.get("superhost", False)
    sel_amenities = request.GET.getlist("amenities")
    sel_facilities = request.GET.getlist("facilities")
    print(instant, superhost)
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

    return render(
        request,
        "rooms/search.html",
        context={
            **form,
            **choices,
        },
    )
