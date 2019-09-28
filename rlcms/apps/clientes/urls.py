from django.conf.urls import url
from rlcms.apps.clientes import views
# from django.contrib.auth.decorators import login_required

app_name = 'clientes'

urlpatterns = [
    url(r'^lista/', views.ClienteList.as_view(), name='listar'),
    url(r'^crear/', views.ClienteCreate.as_view(), name='crear'),
    url(r'^editar/(?P<pk>\d+)/$', views.ClienteUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', views.ClienteDelete.as_view(), name='eliminar'),
]
