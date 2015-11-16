from django.conf.urls import url
from wolf import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^templates$', views.templates, name='templates'),
    url(r'^templates/(?P<templateId>\d+)$', views.template_edit, name='template-edit'),
    url(r'^parse$', views.parse, name='parse'),
    url(r'^solve/(?P<solutionId>\d+)$', views.solve, name='solve'),
    url(r'^run/(?P<solutionId>\d+)$', views.run, name='run'),
]
