import uuid

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from klanad.models import Product, ProductGroup


def groups(request: HttpRequest) -> HttpResponse:
    """Return a list of groups."""
    return render(request, "groups.html", {"groups": ProductGroup.objects.all()})


def group(request: HttpRequest, group_id: uuid) -> HttpResponse:
    """Return a single product group."""
    return render(request, "group.html", {"group": ProductGroup.objects.get(id=group_id)})


def products(request: HttpRequest) -> HttpResponse:
    """Return a list of products."""
    return render(request, "products.html", {"products": Product.objects.all()})


def product(request: HttpRequest, product_id: uuid) -> HttpResponse:
    """Return a single product."""
    return render(request, "product.html", {"product": Product.objects.get(id=product_id)})
