# Generated by Django 4.1 on 2024-06-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0005_alter_block_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="view_3d",
            field=models.URLField(
                blank=True,
                error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
                max_length=500,
                null=True,
            ),
        ),
    ]
