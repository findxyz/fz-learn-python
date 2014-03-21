from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite.views import hello, home, hours_ahead
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', home),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
