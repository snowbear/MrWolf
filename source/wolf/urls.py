from django.conf.urls import patterns, url
from wolf import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^parse$', views.parse, name='parse'),
    url(r'^solve/(?P<solutionId>\d+)$', views.solve, name='solve'),
    url(r'^run/(?P<solutionId>\d+)$', views.run, name='run'),
)
