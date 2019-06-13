# Generated by Django 2.2.2 on 2019-06-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("klanad", "0008_auto_20190609_1212")]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description_de",
            field=models.TextField(
                blank=True, help_text="A description for the product.", null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="description_en",
            field=models.TextField(
                blank=True, help_text="A description for the product.", null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="description_fr",
            field=models.TextField(
                blank=True, help_text="A description for the product.", null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="description_nl",
            field=models.TextField(
                blank=True, help_text="A description for the product.", null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title_de",
            field=models.CharField(
                help_text="The title of the product.", max_length=256, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title_en",
            field=models.CharField(
                help_text="The title of the product.", max_length=256, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title_fr",
            field=models.CharField(
                help_text="The title of the product.", max_length=256, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="title_nl",
            field=models.CharField(
                help_text="The title of the product.", max_length=256, null=True
            ),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="description_de",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="description_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="description_fr",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="description_nl",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="title_de",
            field=models.CharField(
                help_text="The name of the product group.", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="title_en",
            field=models.CharField(
                help_text="The name of the product group.", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="title_fr",
            field=models.CharField(
                help_text="The name of the product group.", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="productgroup",
            name="title_nl",
            field=models.CharField(
                help_text="The name of the product group.", max_length=50, null=True
            ),
        ),
    ]
