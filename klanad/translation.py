from modeltranslation.translator import register, TranslationOptions
from klanad.models import ProductGroup, Product


@register(ProductGroup)
class ProductGroupTranslationOptions(TranslationOptions):
    """Translation fields for ProductGroup."""

    fields = ('title', 'description',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    """Translation fields for Product."""

    fields = ('title', 'description',)
