from django.urls import path
from user.views import UserAPI
from user.views.user_views import RegisterAPI

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register-api"),
]
