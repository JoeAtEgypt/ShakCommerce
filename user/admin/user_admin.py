from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_superuser",
    )
    readonly_fields = ("date_joined", "last_login")
    ordering = ("date_joined",)
