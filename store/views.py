from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Collection
from .serializations import ProductSerializer, CollectionSerializer


# Create your views here.
@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True, context={"request": request})
    return Response(serializer.data)


@api_view()
def collection_detail(request, pk):
    collection = Collection.objects.get(id=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)
