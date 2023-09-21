from django.contrib import admin
from . import models
from django.db.models import Count

# Register your models here.


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "total_products"]

    def total_products(self, collection):
        return collection.product_set.count()


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer_name"]
    list_select_related = ["customer"]

    def customer_name(self, order):
        return order.customer.first_name + " " + order.customer.last_name
