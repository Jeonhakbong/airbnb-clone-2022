from django.shortcuts import render  # allows us to send response with html inside.
from . import models

# from django.http import HttpResponse


# view need to return the response
def all_rooms(request):
    # print(dir(request.GET))
    # print(request.GET)  # we can get quety dict of the request. (convention like page.)
    page = int(request.GET.get("page", 1))  # default is 1.
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    rooms = models.Room.objects.all()[offset:limit]

    return render(
        request,
        "home/all_rooms.html",
        context={
            "rooms": rooms,
        },
    )
