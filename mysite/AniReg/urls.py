from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    url(r'^$', views.post_list, name='post_list'),
#    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
#    url(r'^post/new/$', views.post_new, name='post_new'),
]
