import uuid

from django.db import models
from django.db.models import CASCADE
from model_utils.models import TimeStampedModel


class Address(models.Model):
    """An Address for a person or entity."""

    street = models.CharField(max_length=100, help_text="The name of the street.", null=True, blank=True)
    number = models.CharField(max_length=25, help_text="The number of the building.", null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        """Meta class."""

        abstract = True


class ContactDetails(models.Model):
    """Contact details for a person or company."""

    email = models.EmailField()
    phone = models.CharField(max_length=30, null=True, blank=True)
    fax = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        """Meta class."""

        abstract = True


class Contact(ContactDetails):
    """A Contact for a company."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    notes = models.TextField(
        help_text="Any notes you want to keep for this contact.", null=True, blank=True
    )

    class Meta:
        """Meta class."""

        app_label = "klanad"

    def __repr__(self) -> str:
        """String representation of a Contact."""
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()


class Company(TimeStampedModel, Address, ContactDetails):
    """A Company."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, help_text="The name of the company.")
    description = models.TextField(null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=CASCADE, null=True, blank=True)
    notes = models.TextField(
        help_text="Any notes you want to keep for this company.", null=True, blank=True
    )

    class Meta:
        """Meta class."""

        app_label = "klanad"

    def __repr__(self) -> str:
        """String representation of a Contact."""
        return f"{self.title} - {self.contact.name}"

    def __str__(self) -> str:
        return self.__repr__()


class Product(TimeStampedModel):
    """A Product."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(help_text="The title of the product.", max_length=256)
    description = models.TextField(
        help_text="A description for the product.", null=True, blank=True
    )
    built_on = models.DateField(
        help_text="The date the product was built or first released.",
        null=True,
        blank=True,
    )
    built_in = models.CharField(
        help_text="The country the product was built in.",
        max_length=50,
        null=True,
        blank=True,
    )
    position = models.PositiveIntegerField(
        help_text="The order in which products are shown, in ascending order.",
        null=True,
        blank=True,
    )
    archived = models.BooleanField(
        default=False, help_text="Products which are archived are not shown."
    )

    # Private fields
    built_by = models.ForeignKey(
        Company,
        help_text="Which company built this product.",
        on_delete=CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        """Meta class."""

        ordering = ("position",)
        app_label = "klanad"

    def __repr__(self) -> str:
        """String representation of a Contact."""
        return f"{self.title}"

    def __str__(self) -> str:
        return self.__repr__()


class ProductImage(TimeStampedModel):
    """An image for a product."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="products")
    product = models.ForeignKey(Product, on_delete=CASCADE)
    position = models.PositiveIntegerField(
        help_text="The order in which images are shown, in ascending order.",
        null=True,
        blank=True,
    )

    class Meta:
        """Meta class."""

        ordering = ("position",)
        app_label = "klanad"

    def __repr__(self) -> str:
        """String representation of a Contact."""
        return f"Image for: {self.product.title} with position: {self.position}"

    def __str__(self) -> str:
        return self.__repr__()
