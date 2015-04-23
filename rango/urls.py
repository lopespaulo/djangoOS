from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^about/$', views.about, name='about'),
    #url(r'^category/(?P<category_name_slug>\w+)$', views.category, name='category'),
    #url(r'^add_category/$', views.add_category, name='add_category'),
    #url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^$', views.index, name='home'),
    url(r'^add_cliente/$', views.add_cliente, name='add_cliente'), # NEW MAPPING!
    url(r'^abrir_os/$', views.add_servico, name='add_os'),
    url(r'^editar_servico/$', views.editar_servico, name='editar_servico'),
    url(r'^editar_servico/(?P<id>\d+)/$', views.editar_servico, name='editar_servico'),
    url(r'^historico/$', views.historico, name='historico'),
    url(r'^add_servico/busca_cliente/$', views.busca_cliente, name='search'),
    url(r'^add_cliente/busca_cliente/$', views.busca_cliente, name='search'),

)