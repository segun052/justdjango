from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
    #return HttpResponse("<h1>Contact Page</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
        "title": "This is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 456, 321, "ADE"],
        "my_html": "<h1>Hello World! </h1>"
    }
    return render(request, "about.html", my_context)
    #return HttpResponse("<h1>About Page</h1>")

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
    #return HttpResponse("<h1>Social Page</h1>")