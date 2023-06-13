from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User

# Create your views here.


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all().values()
        return Response(users)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"message": "user deleted."})


# Create an actual action, rendering a page.
