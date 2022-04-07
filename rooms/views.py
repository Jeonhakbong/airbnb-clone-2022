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
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        context={
            "city": city,
            "countries": countries,
            "room_types": room_types,
        },
    )
