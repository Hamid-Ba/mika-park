# Generated by Django 4.1 on 2024-06-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("siteinfo", "0004_critic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="critic",
            name="email",
            field=models.EmailField(
                blank=True, max_length=125, null=True, verbose_name="پست الکترونیک"
            ),
        ),
    ]
