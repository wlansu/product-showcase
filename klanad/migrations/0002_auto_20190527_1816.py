# Generated by Django 2.2.1 on 2019-05-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("klanad", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="city",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="country",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="fax",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="number",
            field=models.CharField(
                blank=True,
                help_text="The number of the building.",
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="phone",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="street",
            field=models.CharField(
                blank=True,
                help_text="The name of the street.",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="fax",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
