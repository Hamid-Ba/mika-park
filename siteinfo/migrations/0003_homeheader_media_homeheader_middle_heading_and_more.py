# Generated by Django 4.1 on 2024-06-27 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0004_media"),
        ("siteinfo", "0002_alter_footerlink_footer_link_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="homeheader",
            name="media",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="media",
                to="gallery.media",
                verbose_name="ویدئو",
            ),
        ),
        migrations.AddField(
            model_name="homeheader",
            name="middle_heading",
            field=models.CharField(
                blank=True, max_length=125, null=True, verbose_name="سر تیتر وسط صفحه"
            ),
        ),
        migrations.AddField(
            model_name="homeheader",
            name="middle_paragraph",
            field=models.TextField(
                blank=True, null=True, verbose_name="پاراگرف وسط صفحه"
            ),
        ),
        migrations.AlterField(
            model_name="homeheader",
            name="paragraph",
            field=models.TextField(blank=True, null=True, verbose_name="پاراگرف"),
        ),
    ]
