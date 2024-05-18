from django.db import models
from django.utils.translation import gettext_lazy as _

class Agent(models.Model):
    """Agent Model"""
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    
    
    class Meta:
        verbose_name = _("نمایندگی")
        verbose_name_plural = _("نمایندگی ها")
        
        
class Agent_Branch(models.Model):
    """Branch Model"""

    name = models.CharField(
        max_length=125, null=False, blank=False, verbose_name="نام شعبه"
    )
    address = models.CharField(
        max_length=225, null=True, blank=True, verbose_name="آدرس"
    )
    
    phones = models.CharField(
        max_length=225, null=True, blank=True, verbose_name="شماره تماس"
    )
    
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, related_name="branches", verbose_name="نمایندگی"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("شعبه نمایندگی")
        verbose_name_plural = _("شعبه های نمایندگی")