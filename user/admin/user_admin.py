from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

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
    fieldsets = (
        (None, {"fields": ("email", "phone_number", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
