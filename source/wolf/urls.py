from django.conf.urls import patterns, url
from wolf import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
