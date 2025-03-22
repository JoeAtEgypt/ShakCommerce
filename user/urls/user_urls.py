from django.urls import path
from user.views import UserAPI

urlpatterns = [
    path("", UserAPI.as_view(), name="user-api"),
]
