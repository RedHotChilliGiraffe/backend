from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from red_hot_chilli_giraffe.accounts.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("email", "username", "phone")
    list_filter = (
        "is_staff",
        "is_superuser",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "last_login",
                    "date_joined",
                )
            },
        ),
        (
            "Permissions",
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
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email", "username", "is_active"),
            },
        ),
        (
            "Password",
            {
                "fields": ("password1", "password2"),
            },
        ),
    )


admin.site.register(User, UserAdmin)
