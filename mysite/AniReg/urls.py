from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.AniRegFormView, name='AniRegFormView'),
    url(r'^form_new/$', views.form_new, name='form_new'),
]
