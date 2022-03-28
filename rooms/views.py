from django.shortcuts import (
    render,
    redirect,
)  # allows us to send response with html inside.
from django.core.paginator import Paginator, EmptyPage
from . import models

# from django.http import HttpResponse

# view need to return the response
def all_rooms(request):
    # pagination.
    page = int(request.GET.get("page", 1))
    room_list = models.Room.objects.all()  # just only create the queryset.
    # QuerySets are lazy – the act of creating a QuerySet doesn’t involve any database activity.

    paginator = Paginator(room_list, per_page=10, orphans=3)

    # With page() method, We can control and handle error as we want.
    try:
        page = paginator.page(page)  # return page object. (vs. get_page())
        return render(
            request,
            "home/all_rooms.html",
            context={  # we can use it in html.
                "page": page,
            },
        )
    except EmptyPage:
        # page = paginator.page(1)
        return redirect("/")
