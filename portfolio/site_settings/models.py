from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string


@register_setting
class SiteSettings(BaseSiteSetting):
    site_name = models.CharField(max_length=100, default='Portfolio')
    site_description = RichTextField(blank=True)
    favicon = models.ForeignKey(
        get_image_model_string(), null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('site_name'),
        FieldPanel('site_description'),
        FieldPanel('favicon'),
    ]