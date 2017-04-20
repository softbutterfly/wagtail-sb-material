# -*- encoding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MaterializeConfig(AppConfig):
    name = 'softbutterfly.wagtail.materialize'
    verbose_name = _('Wagtail Materialize')

    label = 'wagtailmaterialize'
