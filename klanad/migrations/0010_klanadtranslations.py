# Generated by Django 2.2.2 on 2019-06-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("klanad", "0009_auto_20190613_1003")]

    operations = [
        migrations.CreateModel(
            name="KlanadTranslations",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "welcome_title",
                    models.CharField(
                        help_text="Title of the welcome message.", max_length=255
                    ),
                ),
                (
                    "welcome_title_de",
                    models.CharField(
                        help_text="Title of the welcome message.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "welcome_title_en",
                    models.CharField(
                        help_text="Title of the welcome message.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "welcome_title_nl",
                    models.CharField(
                        help_text="Title of the welcome message.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "welcome_title_fr",
                    models.CharField(
                        help_text="Title of the welcome message.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "welcome_message",
                    models.TextField(help_text="Message shown on the landing page."),
                ),
                (
                    "welcome_message_de",
                    models.TextField(
                        help_text="Message shown on the landing page.", null=True
                    ),
                ),
                (
                    "welcome_message_en",
                    models.TextField(
                        help_text="Message shown on the landing page.", null=True
                    ),
                ),
                (
                    "welcome_message_nl",
                    models.TextField(
                        help_text="Message shown on the landing page.", null=True
                    ),
                ),
                (
                    "welcome_message_fr",
                    models.TextField(
                        help_text="Message shown on the landing page.", null=True
                    ),
                ),
                (
                    "footer_email_me",
                    models.CharField(
                        help_text="Message to email the owner of the site.",
                        max_length=100,
                    ),
                ),
                (
                    "footer_email_me_de",
                    models.CharField(
                        help_text="Message to email the owner of the site.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "footer_email_me_en",
                    models.CharField(
                        help_text="Message to email the owner of the site.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "footer_email_me_nl",
                    models.CharField(
                        help_text="Message to email the owner of the site.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "footer_email_me_fr",
                    models.CharField(
                        help_text="Message to email the owner of the site.",
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        )
    ]
