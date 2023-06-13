from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.


def users(request):
    # return HttpResponse("Hi th_ere!")
    template = loader.get_template("usersindex.html")
    return HttpResponse(template.render())


# Create an actual action, rendering a page.
