from django.conf.urls import url
from . import views

#Here we're importing Django's function url and all of our views from the blog application. 

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

#The last part, name='post_list', is the name of the URL that will be used to identify the view.
#This can be the same as the name of the view but it can also be something completely different.
