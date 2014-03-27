from django.conf.urls import patterns, include, url
from books.views import search, contact, contact_thanks

urlpatterns = patterns('',
    # url('^search_form/$', search_form),
    url('^search/$', search),
    url('^contact/$', contact),
    url('^contact/thanks/$', contact_thanks),
)
