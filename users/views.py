from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Create your views here.


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all().values()
        return Response(users)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"message": "user deleted."})

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user information updated"})

        return Response({"message": "something went wrong with the serializer"})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f"User object: {serializer}")
            return Response({"message": "User added"})

        return Response({"message": "something went wrong with the serializer"})


# Create an actual action, rendering a page.
