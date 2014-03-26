from django.conf.urls import patterns, include, url
from books.views import search_form, search

urlpatterns = patterns('',
    url('^search_form/$', search_form),
    url('^search/$', search),
)
