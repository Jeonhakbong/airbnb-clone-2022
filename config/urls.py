"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # we need to include urls in other app.
from django.conf import settings  # set 'from root' clearly
from django.conf.urls.static import static  # static() : help to serve static files


# we don't want our urls.py file make bigger.
# we need to 'divide and conquer' it in each app. folder.
urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:  # Developement mode : serve files in my folder
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
