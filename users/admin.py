from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # import models( is in same folder as the admin )

# Register your models here.
@admin.register(
    models.User
)  # decorator == admin.site.register(models.User, CustomerUserAdmin)
class CustomUserAdmin(UserAdmin):  # Default UserAdmin is already existed.

    """Custom User Admin"""

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "superhost",
        "language",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)
