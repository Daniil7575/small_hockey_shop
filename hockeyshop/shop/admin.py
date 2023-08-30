from django.contrib import admin
from . import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "owner")

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Profile)
admin.site.register(models.ItemPhoto)
