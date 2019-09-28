# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from rlcms.apps.clientes.models import Cliente
from rlcms.apps.clientes.forms import ClienteForm
# Create your views here.


class ClienteList(generic.ListView):
    model = Cliente
    template_name = 'clientes/list.html'
    paginate_by = 10


class ClienteCreate(generic.CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('clientes:listar')


class ClienteUpdate(generic.UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('clientes:listar')


class ClienteDelete(generic.DeleteView):
    model = Cliente
    template_name = 'clientes/delete.html'
    success_url = reverse_lazy('clientes:listar')
