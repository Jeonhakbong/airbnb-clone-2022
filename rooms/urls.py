from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path(
        "<int:pk>", views.RoomDetail.as_view(), name="detail"
    ),  # detail take argument "pk"
    path(
        "search", views.SearchView.as_view(), name="search"
    ),  # we can use name in html.
]
