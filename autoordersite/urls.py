from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # for any url other than admin, look in ../orderer/urls.py
    url(r'', include('orderer.urls')),
]
