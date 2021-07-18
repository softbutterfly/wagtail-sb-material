# -*- encoding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WagtailSbMaterialConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'wagtail_sb_material'
    verbose_name = _('Wagtail Materialize')

    label = 'wagtailmaterialize'
