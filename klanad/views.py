import uuid

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

from klanad.models import Product, ProductGroup, KlanadTranslations, GroupContainer


def containers(request: HttpRequest) -> HttpResponse:
    """Return a list of containers."""
    try:
        translation = KlanadTranslations.objects.all()[0]
        context = {
            "containers": GroupContainer.objects.all(),
            "welcome_title": translation.welcome_title,
            "welcome_message": translation.welcome_message,
        }
    except IndexError:
        context = {
            "containers": GroupContainer.objects.all(),
        }

    return render(request, "containers.html", context)


def groups(request: HttpRequest) -> HttpResponse:
    """Return a list of groups."""
    return render(
        request, "groups.html", {"groups": ProductGroup.objects.filter(archived=False)}
    )


def group(request: HttpRequest, group_id: uuid) -> HttpResponse:
    """Return a single product group."""
    try:
        return render(
            request, "group.html", {"group": ProductGroup.objects.get(id=group_id)}
        )
    except ProductGroup.DoesNotExist:
        raise Http404()


def products(request: HttpRequest) -> HttpResponse:
    """Return a list of products."""
    return render(
        request, "products.html", {"products": Product.objects.filter(archived=False)}
    )


def product(request: HttpRequest, product_id: uuid) -> HttpResponse:
    """Return a single product."""
    try:
        return render(
            request, "product.html", {"product": Product.objects.get(id=product_id)}
        )
    except Product.DoesNotExist:
        raise Http404()
