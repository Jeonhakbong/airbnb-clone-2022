from django.http import Http404
from django.utils import timezone
from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import redirect, render
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


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        # print(room)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()  # we can also use http404 status.
