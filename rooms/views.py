import math
from django.shortcuts import render  # allows us to send response with html inside.
from . import models

# from django.http import HttpResponse


# view need to return the response
def all_rooms(request):
    # pagination.
    page = int(request.GET.get("page", 1) or 1)
    page_size = 10

    limit = page_size * page
    offset = limit - page_size
    rooms = models.Room.objects.all()[offset:limit]

    page_count = math.ceil(models.Room.objects.count() / page_size)

    return render(
        request,
        "home/all_rooms.html",
        context={  # we can use it in html.
            "rooms": rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
