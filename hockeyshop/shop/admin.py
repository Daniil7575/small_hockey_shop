from django.contrib import admin
from django.contrib.auth.models import User

from . import models


# class OwnerAdminInline(admin.TabularInline):
#     model = User


class ProfileAdmin(admin.ModelAdmin):
    # inlines = (OwnerAdminInline,)
    search_fields = ("user__username",)
    list_display = ("user_name", "phone")

    @admin.display(description="Имя пользователя")
    def user_name(self, obj):
        return obj.user.username


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "owner")


admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Profile, ProfileAdmin)
