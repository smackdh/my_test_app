from django.urls import path
from .views import UserListCreateAPIView, userDetailAPIView

urlpatterns = [path("users/", views.users, name="users")]
