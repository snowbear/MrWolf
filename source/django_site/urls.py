from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('wolf.urls', namespace="wolf")),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
