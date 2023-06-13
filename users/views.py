from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import User

# Create your views here.


def users(request):
    users = User.objects.all().values()
    template = loader.get_template("usersindex.html")
    context = {"users": users}
    return HttpResponse(template.render(context, request))


# Create an actual action, rendering a page.
