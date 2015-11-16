from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('wolf.urls', namespace="wolf")),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
