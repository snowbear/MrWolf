from django.conf.urls import patterns, url
from wolf import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^solve$', views.solve, name='solve'),
    url(r'^run$', views.run, name='run'),
)
