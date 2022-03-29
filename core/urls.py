from django.urls import path
from rooms import views as room_views

app_name = "core"  # we can find core urls by using 'namespace' in config urls.

# urls for home, login, logout and so on.
urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),  # home.
]
