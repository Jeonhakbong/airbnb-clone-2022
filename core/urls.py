from django.urls import path
from rooms import views as room_views

app_name = "core"

# urls of home, login, logout and so on.
urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]
