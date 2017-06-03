from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main$', views.main, name='main'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^registration$', views.registration, name='registration')
]
