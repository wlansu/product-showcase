from django.contrib import admin
from django.utils.html import format_html

from modeltranslation.admin import TranslationAdmin

from klanad.models import Product, Company, Contact, ProductImage, ProductGroupImage, ProductGroup, KlanadTranslations


admin.site.register(Company)
admin.site.register(Contact)


@admin.register(KlanadTranslations)
class KlanadTranslationAdmin(TranslationAdmin):
    """Admin for the various dynamic fields of the website."""


class ProductImageInline(admin.TabularInline):
    """Inline ProductImage for the Product admin."""

    model = ProductImage
    readonly_fields = ('preview', )

    def preview(self, obj: ProductImage) -> str:
        """Display a preview of the image."""
        html = '<a href="{url}" target="_blank"><img src="{url}" /></a>'
        return format_html(''.join(html.format(url=obj.image.url)))


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    """Product admin page."""

    list_display = ("title", "position", "archived")
    list_editable = ("position", "archived")
    inlines = [
        ProductImageInline,
    ]


class ProductGroupImageInline(admin.TabularInline):
    """Inline ProductImage for the ProductGroup admin."""

    model = ProductGroupImage
    readonly_fields = ('preview', )

    def preview(self, obj: ProductImage) -> str:
        """Display a preview of the image."""
        html = '<a href="{url}" target="_blank"><img src="{url}" /></a>'
        return format_html(''.join(html.format(url=obj.image.url)))


@admin.register(ProductGroup)
class ProductGroupAdmin(TranslationAdmin):
    """Product admin page."""

    list_display = ("title", "position", "archived")
    list_editable = ("position", "archived")
    inlines = [
        ProductGroupImageInline,
    ]
