from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    readonly_fields = ("date_joined", "last_login")
