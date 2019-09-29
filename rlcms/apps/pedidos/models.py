# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rlcms.apps.clientes.models import Cliente
# from rlcms.apps.productos.models import Producto
# Create your models here.


class TipoPago(models.Model):
    descripcion = models.CharField(max_length=30)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    referencia = models.PositiveSmallIntegerField()


class Impuesto(models.Model):
    descripcion = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['-id']


class Factura(models.Model):
    empleado = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        Cliente, null=False, blank=False, on_delete=models.CASCADE)
    tipo_pago = models.ManyToManyField(TipoPago, blank=True)
    impuesto = models.ForeignKey(
        Impuesto, null=False, blank=False, on_delete=models.CASCADE)
    # producto = models.ManyToManyField(Producto, null=False, blank=False)


class Credito(models.Model):
    factura = models.ForeignKey(
        Factura, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cancelado = models.BooleanField(default=False)
