from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from common.mixins.slug_mixin import SlugModelMixin
from user.models.user_manager import UserManager


class User(AbstractBaseUser, SlugModelMixin, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneNumberField(unique=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    slug_attr_name = "username"

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = UserManager()

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
