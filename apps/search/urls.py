from django.conf.urls import url
from django.contrib import admin

from apps.search import views

urlpatterns = [
    url('search/$', views.search, name='search')
]
