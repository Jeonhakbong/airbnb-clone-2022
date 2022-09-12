from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms

# from django_countries import countries


# we don't need to programming like return render. Just configurate it with django with CBV.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    context_object_name = "rooms"  # change 'object_list' to 'rooms'.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now

        return context


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


class SearchView(View):

    """SearchView Definition"""

    def get(self, request):
        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)  # bounded form.

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                # filtering.
                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    # superhost is not in room models. so we use foreign key.
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                filter_args["country"] = country

                # Paginator need ordered elements.
                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                paginator = Paginator(qs, 10, orphans=3)
                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)
                # print(vars(rooms.paginator))
                # print(dir(rooms.paginator))

                return render(
                    request,
                    "rooms/search.html",
                    context={
                        "form": form,
                        "rooms": rooms,
                    },
                )
        else:
            form = forms.SearchForm()  # unbounded form.

        return render(
            request,
            "rooms/search.html",
            context={
                "form": form,
            },
        )
