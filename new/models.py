from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from gallery import models as gallery_models


class New(models.Model):
    """New Model"""

    title = models.CharField(max_length=85, blank=False, null=False, verbose_name="عنوان")
    slug = models.SlugField(max_length=170, blank=False, null=False, verbose_name="اسلاگ")
    short_desc = models.CharField(max_length=300, blank=True, null=True, verbose_name="توضیحات کوتاه")
    desc = RichTextField(blank=True, null=True, verbose_name="توضیحات")
    image_alt = models.CharField(max_length=72, blank=True, null=True)
    image_title = models.CharField(max_length=125, blank=True, null=True)
    publish_date = models.DateTimeField(
        null=False, blank=False, default=timezone.now, db_index=True, verbose_name="زمان انتشار"
    )

    image = models.ForeignKey(
        gallery_models.Gallery,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="news",
        verbose_name="تصویر"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _("خبر")
        verbose_name_plural = _("اخبار")