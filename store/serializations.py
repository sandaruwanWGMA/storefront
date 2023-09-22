from rest_framework import serializers
from .models import Product, Collection


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "unit_price", "collection"]

        collection = serializers.HyperlinkedIdentityField(view_name="collection-detail")


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["title"]
