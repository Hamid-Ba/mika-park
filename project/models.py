import os
from ckeditor.fields import RichTextField
from uuid import uuid4
from django.utils.translation import gettext_lazy as _

from django.db import models

from gallery import models as gallery_models


def project_image_file_path(instance, filename):
    """Generate file path for project image"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "project", filename)


def csv_file_path(instance, filename):
    """Generate file path for media"""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid4()}.{ext}"

    return os.path.join("uploads", "csv", filename)


class Feature(models.Model):
    """Features Model"""

    title = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="عنوان"
    )
    logo = models.ForeignKey(
        gallery_models.Gallery,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="project_feature_logo",
        verbose_name="تصویر",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _("امکانات")
        verbose_name_plural = _("امکانات")


class Project(models.Model):
    """Project Model"""

    class Type(models.TextChoices):
        Processing = "P", "پروژهای در حال انجام"
        Done = "D", "پروژهای انجام شده"

    title = models.CharField(max_length=150, verbose_name="عنوان")
    desc = RichTextField(blank=True, null=True, verbose_name="توضیحات")
    image = models.ImageField(
        null=False, upload_to=project_image_file_path, verbose_name="تصویر"
    )
    type = models.CharField(max_length=2, choices=Type.choices, default=Type.Processing)
    view_3d = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="لینک نمای ۳ بعدی",
        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    )
    google_map_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="لینک گوگل مپ",
        error_messages={"invalid": "مقدار وارد شده صحیح نم باشد"},
    )

    gallery = models.ManyToManyField(
        gallery_models.Gallery, related_name="projects", verbose_name="گالری"
    )

    media = models.ManyToManyField(
        gallery_models.Media, related_name="projects", verbose_name="مدیا"
    )

    features = models.ManyToManyField(
        Feature, related_name="projects", verbose_name="امکانات"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("پروژه")
        verbose_name_plural = _("پروژه ها")


class Project_Specification(models.Model):
    """Specifications Model"""

    key = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="مشخصه"
    )
    value = models.CharField(
        max_length=225, null=False, blank=False, verbose_name="مقدار"
    )

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="specs", verbose_name="پروژه"
    )

    def __str__(self):
        return f"{self.project.title}-{self.key}"

    class Meta:
        verbose_name = _("مشخصه پروژه")
        verbose_name_plural = _("مشخصات پروژه ها")


class Project_Property(models.Model):
    """Properties Model"""

    value = models.CharField(
        max_length=225, null=False, blank=False, verbose_name="مقدار"
    )

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="props", verbose_name="پروژه"
    )

    def __str__(self):
        return f"{self.project.title}-{self.value}"

    class Meta:
        verbose_name = _("ویژگی پروژه")
        verbose_name_plural = _("ویژگی پروژه ها")


class Block(models.Model):
    """Block Model"""

    title = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="نام"
    )

    main_csv_data = models.FileField(
        null=True, blank=True, upload_to=csv_file_path, verbose_name="فایل csv اول"
    )

    child_csv_file = models.FileField(
        null=True, blank=True, upload_to=csv_file_path, verbose_name="فایل csv دوم"
    )

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="blocks", verbose_name="پروژه"
    )

    class Meta:
        verbose_name = _("بلوک")
        verbose_name_plural = _("بلوک ها")


class Block_Specification(models.Model):
    """Specifications Model"""

    key = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="مشخصه"
    )
    value = models.CharField(
        max_length=225, null=False, blank=False, verbose_name="مقدار"
    )

    block = models.ForeignKey(
        Block, on_delete=models.CASCADE, related_name="specs", verbose_name="بلوک"
    )

    def __str__(self):
        return f"{self.block.title}-{self.key}"

    class Meta:
        verbose_name = _("مشخصه بلوک")
        verbose_name_plural = _("مشخصات بلوک ها")


class MainChart(models.Model):
    """Main Chart Model"""

    index = models.PositiveBigIntegerField(
        null=False, blank=False, verbose_name="شناسه"
    )
    label = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="عنوان"
    )
    percent = models.PositiveBigIntegerField(
        null=False, blank=False, verbose_name="درصد"
    )
    color = models.CharField(
        max_length=225, null=False, blank=False, verbose_name="رنگ"
    )

    block = models.ForeignKey(
        Block, on_delete=models.CASCADE, related_name="charts", verbose_name="بلوک"
    )

    def __str__(self) -> str:
        return f"{self.index} {self.label}"

    class Meta:
        verbose_name = _("نمودار اصلی")
        verbose_name_plural = _("نمودارهای اصلی")


class ChildChart(models.Model):
    """Child Chart Model"""

    index = models.PositiveBigIntegerField(
        null=False, blank=False, verbose_name="شناسه"
    )
    label = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="عنوان"
    )
    percent = models.PositiveBigIntegerField(
        null=False, blank=False, verbose_name="درصد"
    )
    color = models.CharField(
        max_length=225, null=False, blank=False, verbose_name="رنگ"
    )

    main = models.ForeignKey(
        MainChart,
        on_delete=models.CASCADE,
        related_name="childs",
        verbose_name="زیرمجموعه",
    )

    def __str__(self) -> str:
        return f"{self.index} {self.label}"

    class Meta:
        verbose_name = _("نمودار زیرمجموعه")
        verbose_name_plural = _("نمودارهای زیرمجموعه")
