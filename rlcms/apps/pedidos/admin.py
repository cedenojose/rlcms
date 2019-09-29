# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from rlcms.apps.pedidos.models import Factura, Credito, TipoPago, Impuesto

# Register your models here.


admin.site.register(Factura)
admin.site.register(Credito)
admin.site.register(TipoPago)
admin.site.register(Impuesto)