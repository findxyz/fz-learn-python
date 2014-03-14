from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite.views import hello, home
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', home),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
)
