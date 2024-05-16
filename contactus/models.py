"""
    contact us models
"""
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.validators import phone_validator


class Message(models.Model):
    """Message Model"""

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
    text = models.CharField(
        max_length=1200, null=False, blank=False, verbose_name="متن پیام"
    )
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ارسال"
    )

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone}"

    class Meta:
        verbose_name = _("درخواست")
        verbose_name_plural = _("درخواست ها")


class Address(models.Model):
    """Address"""

    address = models.CharField(
        max_length=225, null=True, blank=True, verbose_name="عنوان"
    )

    class Meta:
        verbose_name = _("آدرس")
        verbose_name_plural = _("آدرس ها")


class Phone(models.Model):
    """Phone"""

    phone = models.CharField(
        max_length=21, null=False, blank=False, verbose_name="شماره تماس"
    )

    class Meta:
        verbose_name = _("شماره تماس")
        verbose_name_plural = _("شماره های تماس")


class Email(models.Model):
    """Email"""

    email = models.EmailField(
        max_length=125, null=False, blank=False, verbose_name="پست الکترونیک"
    )

    class Meta:
        verbose_name = _("پست الکترونیک")
        verbose_name_plural = _("پست های الکترونیک")
