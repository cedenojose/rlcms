from django.conf.urls import url

from rlcms.apps.egresos import views

urlpatterns = [
    url(r'^lista/$', views.EgresoList.as_view(), name='listar'),
    url(r'^crear/$', views.EgresoCreate.as_view(), name='crear'),
    url(r'^editar/(?P<pk>\d+)/$', views.EgresoUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', views.EgresoDelete.as_view(), name='eliminar'),
]
