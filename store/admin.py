from django.contrib import admin
from . import models
from django.db.models import Count

# Register your models here.


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "total_products"]

    def total_products(self, collection):
        return collection.product_set.count()
