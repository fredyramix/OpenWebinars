from django.conf.urls import patterns, url
from album import views


urlpatterns = patterns('',
                       url(r'^$', views.first_view, name='first-view'),
                       )