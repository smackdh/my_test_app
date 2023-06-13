from django.urls import path
from users.views import UserListAPIView

urlpatterns = [
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("users/<int:pk>", UserListAPIView.as_view(), name="user-detail"),
]
