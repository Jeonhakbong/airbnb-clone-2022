from datetime import datetime
from django.shortcuts import render  # allows us to send response with html inside.
from django.http import HttpResponse


# view need to return the response
def all_rooms(request):
    # print(dir(request))  # we can check the request.
    # now = datetime.now()
    # HttpResponse(content=f"<h1>hello, It's {now}.")
    return render(request, "hello.html")
