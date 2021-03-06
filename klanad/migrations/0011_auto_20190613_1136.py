# Generated by Django 2.2.2 on 2019-06-13 11:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [("klanad", "0010_klanadtranslations")]

    operations = [
        migrations.CreateModel(
            name="GroupContainer",
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
                        help_text="The title of the product.", max_length=256
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productgroup",
            name="container",
            field=models.ForeignKey(
                blank=True,
                help_text="Which container does this group belong to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="klanad.GroupContainer",
            ),
        ),
    ]
