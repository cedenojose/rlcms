# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TipoCliente(models.Model):
    nomenclatura = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=13)

    def __str__(self):
        return '{} ({})'.format(self.descripcion, self.nomenclatura)


class Cliente(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True, unique=True)
    tipo_cliente = models.ForeignKey(
        TipoCliente, null=False, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    domicilio = models.TextField()

    def __str__(self):
        return '{}-{} {}'.format(self.tipo_cliente, self.codigo, self.nombre)
