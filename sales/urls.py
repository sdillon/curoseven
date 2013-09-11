from django.conf.urls.defaults import patterns, include, url

from c7.sales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)