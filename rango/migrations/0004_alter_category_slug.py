# Generated by Django 4.1 on 2023-01-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rango", "0003_alter_category_options_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
