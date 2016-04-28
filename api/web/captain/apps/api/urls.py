from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^stations$', views.stations, name='stations_list'),
]