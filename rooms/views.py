from django.shortcuts import render  # allows us to send response with html inside.
from . import models

# from django.http import HttpResponse


# view need to return the response
def all_rooms(request):
    rooms = models.Room.objects.all()

    return render(
        request,
        "home/all_rooms.html",
        context={
            "rooms": rooms,
        },
    )
