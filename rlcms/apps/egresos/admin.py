# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rlcms.apps.egresos.models import Egreso, UnidadMedida

# Register your models here.

admin.site.register(Egreso)
admin.site.register(UnidadMedida)
