# Generated by Django 2.2.2 on 2019-06-06 12:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [("klanad", "0004_auto_20190606_1011")]

    operations = [
        migrations.CreateModel(
            name="ProductGroup",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="The name of the company.", max_length=50
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(upload_to="products"),
        ),
        migrations.AddField(
            model_name="product",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="klanad.ProductGroup",
            ),
        ),
    ]
