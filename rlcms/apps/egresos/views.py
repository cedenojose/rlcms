# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from rlcms.apps.egresos.models import Egreso
from rlcms.apps.egresos.forms import EgresoForm

# Create your views here.


class EgresoList(generic.ListView):
    model = Egreso
    template_name = 'egresos/list.html'


class EgresoCreate(generic.CreateView):
    model = Egreso
    form_class = EgresoForm
    template_name = 'egresos/form.html'
    success_url = reverse_lazy('egresos:listar')


class EgresoUpdate(generic.UpdateView):
    model = Egreso
    form_class = EgresoForm
    template_name = 'egresos/form.html'
    success_url = reverse_lazy('egresos:listar')


class EgresoDelete(generic.DeleteView):
    model = Egreso
    template_name = 'egresos/delete.html'
    success_url = reverse_lazy('egresos:listar')
