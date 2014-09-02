from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'unit/', include('apps.units.urls', namespace='units')),
    url(r'api/v1/', include('apps.units.api_urls', namespace='api')),
)
