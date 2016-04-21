from django.conf.urls import patterns, url
from . import views

urlpatterns = [
        url(r'^helloworld/$', views.index, name='index'),
	url(r'^angular/$', views.angular, name='angular'),
	url(r'^database/$', views.database, name='database'),]

