# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rlcms.apps.clientes.models import Cliente, TipoCliente
# Register your models here.

admin.site.register(Cliente)
admin.site.register(TipoCliente)
