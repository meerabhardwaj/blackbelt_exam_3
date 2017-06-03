from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.travels, name='dashboard'),
    url(r'^destination/(?P<id>\d+)', views.destination, name='destination'),
    url(r'^add$', views.add, name='add'),
    url(r'^create', views.create, name='create'),
    url(r'^join/(?P<id>\d+)', views.join, name='join')
]
