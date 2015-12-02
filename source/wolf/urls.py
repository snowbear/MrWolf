from django.conf.urls import url
from wolf import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^templates$', views.templates, name='templates'),
    url(r'^templates/(?P<template_id>\d+)$', views.template_edit, name='template-edit'),
    url(r'^parse$', views.parse, name='parse'),
    url(r'^solve/(?P<solution_id>\d+)$', views.solve, name='solve'),
    url(r'^run/(?P<solution_id>\d+)$', views.run, name='run'),
]
