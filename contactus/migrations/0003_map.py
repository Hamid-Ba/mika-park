# Generated by Django 4.1 on 2024-06-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contactus", "0002_alter_address_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Map",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "map",
                    models.URLField(
                        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
                        max_length=500,
                        verbose_name="لینک گوگل مپ",
                    ),
                ),
            ],
            options={
                "verbose_name": "مپ",
                "verbose_name_plural": "مپ ها",
            },
        ),
    ]
