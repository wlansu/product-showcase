from django.contrib import admin
from django.utils.html import format_html

from klanad.models import Product, Company, Contact, ProductImage, ProductGroupImage, ProductGroup


admin.site.register(Company)
admin.site.register(Contact)


class ProductImageInline(admin.TabularInline):
    """Inline ProductImage for the Product admin."""

    model = ProductImage
    readonly_fields = ('preview', )

    def preview(self, obj: ProductImage) -> str:
        """Display a preview of the image."""
        html = '<a href="{url}" target="_blank"><img src="{url}" /></a>'
        return format_html(''.join(html.format(url=obj.image.url)))


class ProductAdmin(admin.ModelAdmin):
    """Product admin page."""

    inlines = [
        ProductImageInline,
    ]


class ProductGroupImageInline(admin.TabularInline):
    """Inline ProductImage for the Product admin."""

    model = ProductGroupImage
    readonly_fields = ('preview', )

    def preview(self, obj: ProductImage) -> str:
        """Display a preview of the image."""
        html = '<a href="{url}" target="_blank"><img src="{url}" /></a>'
        return format_html(''.join(html.format(url=obj.image.url)))


class ProductGroupAdmin(admin.ModelAdmin):
    """Product admin page."""

    inlines = [
        ProductGroupImageInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
