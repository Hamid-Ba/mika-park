# Generated by Django 4.1 on 2024-07-03 16:46

from django.db import migrations, models
import django.db.models.deletion
import project.models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0007_alter_project_google_map_url_alter_project_view_3d"),
    ]

    operations = [
        migrations.AddField(
            model_name="block",
            name="child_csv_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=project.models.csv_file_path,
                verbose_name="فایل csv دوم",
            ),
        ),
        migrations.AddField(
            model_name="block",
            name="main_csv_data",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=project.models.csv_file_path,
                verbose_name="فایل csv اول",
            ),
        ),
        migrations.CreateModel(
            name="MainChart",
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
                ("index", models.PositiveBigIntegerField(verbose_name="شناسه")),
                ("label", models.CharField(max_length=125, verbose_name="عنوان")),
                ("percent", models.PositiveBigIntegerField(verbose_name="درصد")),
                ("color", models.CharField(max_length=225, verbose_name="رنگ")),
                (
                    "block",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="charts",
                        to="project.block",
                        verbose_name="بلوک",
                    ),
                ),
            ],
            options={
                "verbose_name": "نمودار اصلی",
                "verbose_name_plural": "نمودارهای اصلی",
            },
        ),
        migrations.CreateModel(
            name="ChildChart",
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
                ("index", models.PositiveBigIntegerField(verbose_name="شناسه")),
                ("label", models.CharField(max_length=125, verbose_name="عنوان")),
                ("percent", models.PositiveBigIntegerField(verbose_name="درصد")),
                ("color", models.CharField(max_length=225, verbose_name="رنگ")),
                (
                    "main",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="childs",
                        to="project.mainchart",
                        verbose_name="زیرمجموعه",
                    ),
                ),
            ],
            options={
                "verbose_name": "نمودار زیرمجموعه",
                "verbose_name_plural": "نمودارهای زیرمجموعه",
            },
        ),
    ]
