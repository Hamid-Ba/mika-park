# Generated by Django 4.1 on 2024-07-04 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0009_rename_main_csv_data_block_type_csv_file_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mainchart",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="charts",
                to="project.charttype",
                verbose_name="نمودار",
            ),
        ),
    ]
