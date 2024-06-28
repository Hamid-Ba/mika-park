# Generated by Django 4.1 on 2024-06-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0002_project_media_project_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="google_map_url",
            field=models.URLField(
                blank=True,
                error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
                max_length=500,
                null=True,
            ),
        ),
    ]
