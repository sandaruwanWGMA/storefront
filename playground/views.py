from django.shortcuts import render
from django.http import HttpResponse
from store.models import Collection, Product
from django.db.models.aggregates import Count


def say_hello(request):
    result = Collection.objects.annotate(count=Count("product"))
    return render(request, "hello.html", {"name": "Mosh", "result": result})
