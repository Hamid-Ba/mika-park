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
        return f"{self.title}-{self.key}"

    class Meta:
        verbose_name = _("امکانات")
        verbose_name_plural = _("امکانات")


class Project(models.Model):
    """Project Model"""

    title = models.CharField(max_length=150, verbose_name="عنوان")
    desc = RichTextField(blank=True, null=True, verbose_name="توضیحات")
    image = models.ImageField(
        null=False, upload_to=project_image_file_path, verbose_name="تصویر"
    )

    gallery = models.ManyToManyField(
        gallery_models.Gallery, related_name="projects", verbose_name="گالری"
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
        return f"{self.project.title}-{self.key}"

    class Meta:
        verbose_name = _("ویژگی پروژه")
        verbose_name_plural = _("ویژگی پروژه ها")
