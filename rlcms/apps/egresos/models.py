# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UnidadMedida(models.Model):
    simbolo = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=15)

    def __str__(self):
        return '{} ({})'.format(self.descripcion, self.simbolo)


class Egreso(models.Model):
    empleado = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(
        UnidadMedida, null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    costo_unitario = models.DecimalField(max_digits=18, decimal_places=2)
    cantidad = models.PositiveSmallIntegerField()
    fecha = models.DateField(auto_now=False)

    def __str__(self):
        return '{} ({})'.format(self.descripcion, self.costo_unitario)
