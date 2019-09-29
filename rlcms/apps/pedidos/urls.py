from django.conf.urls import url
from rlcms.apps.pedidos import views
urlpatterns = [
    url(r'^factura/$', views.FacturaList , name='lista')
]