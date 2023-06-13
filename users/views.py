from django.shortcuts import render

from django.http import JsonResponse
from django.template import loader
from .models import User

# Create your views here.


def users(request):
    if request.method == "GET":
        users = User.objects.all().values()
        json_data = list(users)
        return JsonResponse(json_data, safe=False)
    elif request.method == "DELETE":
        user = User.objects.all()
    else:
        return JsonResponse({"message": "Invalid request method"})


# Create an actual action, rendering a page.
