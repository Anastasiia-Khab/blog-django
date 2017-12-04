from django.conf.urls import url
from . import views

#Here we're importing Django's function url and all of our views from the blog application.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

#The last part, name='post_list', is the name of the URL that will be used to identify the view.
#This can be the same as the name of the view but it can also be something completely different.
