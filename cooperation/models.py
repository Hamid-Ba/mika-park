import os
from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.validators import phone_validator


def cv_file_path(instance, filename):
    """Generate file path for cooperation cv"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "cvs", filename)

class CooperationType(models.Model):
    """Cooperation Type"""
    
    title = models.CharField(max_length=125, null=False, blank=False, verbose_name="نوع همکاری")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _("نوع همکاری")
        verbose_name_plural = _("انواع همکاری")

class CooperationRequest(models.Model):
    """Cooperation Model"""
    
    first_name = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="نام"
    )
    
    last_name = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="نام خانوادگی"
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
    
    cv = models.FileField(null=True, blank=True, upload_to=cv_file_path, verbose_name="رزومه")
    message = models.TextField(blank=True, null=True, max_length=1200, verbose_name="پیام")
    
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ارسال"
    )
    
    type = models.ForeignKey(CooperationType, on_delete=models.CASCADE, verbose_name="نوع همکاری")
    
    class Meta:
        verbose_name = _("درخواست همکاری")
        verbose_name_plural = _("درخواست های همکاری")