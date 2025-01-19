# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser,Blog

# # Register your models here.
# class CustomUserAdmin(UserAdmin):
#     list_display = ("username","email","first_name","last_name","bio","facebook","instagram","profile_pic")

# admin.site.register(CustomUser,CustomUserAdmin)

# class BlogAdmin(admin.ModelAdmin):
#     list_display = ("title", "category", "author", "is_draft")

# admin.site.register(Blog,BlogAdmin)

####################################################################################################################
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Blog
from django.utils.translation import gettext_lazy as _

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "profile_pic")
    
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'bio', 'profile_pic', 'facebook', 'twitter', 'instagram', 'youtube')}),
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

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('bio', 'profile_pic', 'facebook', 'twitter', 'instagram', 'youtube')
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","author" ,"is_draft", "category", "created_at")

admin.site.register(Blog, BlogAdmin)