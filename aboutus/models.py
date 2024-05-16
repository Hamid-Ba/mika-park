"""
    about us models
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from gallery.models import Gallery


class AboutUs(models.Model):
    """About Us Model"""

    title = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="عنوان"
    )
    text = models.TextField(blank=True, null=True, verbose_name="متن")

    image = models.ForeignKey(
        Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="about_image",
        verbose_name="تصویر",
    )

    class Meta:
        verbose_name = _("درباره ما")
        verbose_name_plural = _("درباره ما")


class AboutUsExtension(models.Model):
    """About Us Extension Model"""

    main_title = models.CharField(
        max_length=72, null=False, blank=False, verbose_name="عنوان اصلی"
    )
    title = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="عنوان"
    )

    class Meta:
        verbose_name = _("افزونه درباره ما")
        verbose_name_plural = _("افزونه های درباره ما")
