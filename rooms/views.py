from django.shortcuts import render  # allows us to send response with html inside.
from django.core.paginator import Paginator
from . import models

# from django.http import HttpResponse

# view need to return the response
def all_rooms(request):
    # pagination.
    page = request.GET.get("page")
    room_list = models.Room.objects.all()  # just only create the queryset.
    # QuerySets are lazy – the act of creating a QuerySet doesn’t involve any database activity.

    paginator = Paginator(room_list, per_page=10, orphans=3)

    page = paginator.get_page(page)  # return page object.

    print(vars(page))  # get dictionary in current page.
    print(vars(page.paginator))
    return render(
        request,
        "home/all_rooms.html",
        context={  # we can use it in html.
            "page": page,
        },
    )
