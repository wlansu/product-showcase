from typing import Dict

from django.http import HttpRequest

from klanad.models import KlanadTranslations


def footer_processor(request: HttpRequest) -> Dict[str, str]:
    """Add the footer email me message to the context of all templates since the footer is included everywhere."""
    try:
        message = KlanadTranslations.objects.all()[0].footer_email_me
        return {"footer_email_me": message}
    except IndexError:
        return {}
