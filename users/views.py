from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def users(request):
    return HttpResponse("Hi there!")

# Create an actual action, rendering a page.
