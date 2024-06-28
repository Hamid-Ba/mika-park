"""
    site info models
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.validators import phone_validator
from gallery.models import Gallery, Media


class HomeHeader(models.Model):
    """Home Header"""

    logo_title = models.CharField(
        max_length=72, null=True, blank=True, verbose_name="عنوان"
    )
    heading = models.CharField(
        max_length=125, null=True, blank=True, verbose_name="سر تیتر"
    )
    heading2 = models.CharField(
        max_length=125, null=True, blank=True, verbose_name="2 سر تیتر"
    )
    paragraph = models.TextField(null=True, blank=True, verbose_name="پاراگرف")
    phone = models.CharField(
        max_length=21,
        null=True,
        blank=True,
        validators=[phone_validator],
        verbose_name="شماره موبایل",
    )
    middle_heading = models.CharField(
        max_length=125, null=True, blank=True, verbose_name="سر تیتر وسط صفحه"
    )
    middle_paragraph = models.TextField(
        null=True, blank=True, verbose_name="پاراگرف وسط صفحه"
    )

    logo = models.ForeignKey(
        Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="logo",
        verbose_name="لوگو",
    )
    heading_image = models.ForeignKey(
        Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="heading",
        verbose_name="تصویر تیتر",
    )
    media = models.ForeignKey(
        Media,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="media",
        verbose_name="ویدئو",
    )

    class Meta:
        verbose_name = _("تیتر صفحه اصلی")
        verbose_name_plural = _("تیتر صفحه اصلی")


class Service(models.Model):
    """Service"""

    title = models.CharField(
        max_length=125, null=True, blank=True, verbose_name="عنوان"
    )
    description = models.CharField(
        max_length=1000, null=True, blank=True, verbose_name="توضیحات"
    )

    logo = models.ForeignKey(
        Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="service_logo",
        verbose_name="لوگو",
    )

    class Meta:
        verbose_name = _("خدمت")
        verbose_name_plural = _("خدمات")


class Feature(models.Model):
    """Feature"""

    title = models.CharField(
        max_length=125, null=True, blank=True, verbose_name="عنوان"
    )

    logo = models.ForeignKey(
        Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="feature_logo",
        verbose_name="تصویر",
    )

    class Meta:
        verbose_name = _("امکان")
        verbose_name_plural = _("امکانات")


class Footer(models.Model):
    """Footer"""

    title = models.CharField(max_length=72, null=True, blank=True, verbose_name="عنوان")
    description = models.CharField(
        max_length=1500, null=True, blank=True, verbose_name="توضیحات"
    )

    logo = models.ForeignKey(
        Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="footer_logo",
        verbose_name="لوگو",
    )

    class Meta:
        verbose_name = _("فوتر")
        verbose_name_plural = _("فوتر")


class FooterLink(models.Model):
    """Footer Link"""

    class FooterLinkType(models.TextChoices):
        FastLink = "F", "لینک سریع"
        ContactUs = "C", "تماس با ما"

    title = models.CharField(max_length=72, null=True, blank=True, verbose_name="عنوان")
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
        verbose_name="لینک",
    )

    footer_link_type = models.CharField(
        max_length=1,
        default=FooterLinkType.FastLink,
        choices=FooterLinkType.choices,
        verbose_name="نوع لینک",
    )

    class Meta:
        verbose_name = _("لینک فوتر")
        verbose_name_plural = _("لینک های فوتر")


class Communication(models.Model):
    """Communication"""

    title = models.CharField(max_length=72, null=True, blank=True, verbose_name="عنوان")
    logo = models.ForeignKey(
        Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="communication_logo",
        verbose_name="لوگو",
    )
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
        verbose_name="لینک",
    )

    class Meta:
        verbose_name = _("راه ارتباطی")
        verbose_name_plural = _("راه های ارتباطی")


class Critic(models.Model):
    """Critic Model"""

    full_name = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="نام کامل"
    )
    phone = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        validators=[phone_validator],
        verbose_name="شماره موبایل",
    )
    email = models.EmailField(
        max_length=125, null=False, blank=False, verbose_name="پست الکترونیک"
    )
    text = models.CharField(
        max_length=1200, null=False, blank=False, verbose_name="متن پیام"
    )
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال")

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone}"

    class Meta:
        verbose_name = _("انتقاد و پیشنهاد")
        verbose_name_plural = _("انتقادات و پیشنهادات")