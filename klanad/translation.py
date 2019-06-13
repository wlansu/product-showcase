from modeltranslation.translator import register, TranslationOptions
from klanad.models import ProductGroup, Product, KlanadTranslations, GroupContainer


@register(ProductGroup)
class ProductGroupTranslationOptions(TranslationOptions):
    """Translation fields for ProductGroup."""

    fields = ("title", "description")


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    """Translation fields for Product."""

    fields = ("title", "description")


@register(KlanadTranslations)
class KlanadTranslationsOptions(TranslationOptions):
    """Translation fields for the various dynamic text fields."""

    fields = ("welcome_title", "welcome_message", "footer_email_me")


@register(GroupContainer)
class GroupContainerTranslationOptions(TranslationOptions):
    """Translation fields for GroupContainer."""

    fields = ("title",)
