from django.conf.urls import patterns, include, url
from myapp.views import hello, home, hours_ahead, current_time

urlpatterns = patterns('',
    url('^$', home),
    url(r'^hello/$', hello),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^current_time/$', current_time),
)
