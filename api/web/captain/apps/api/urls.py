from django.conf.urls import url
from rest_framework import routers

from . import views

# Define REST router, and add it in django regular urls
router = routers.DefaultRouter()
router.register(r'stations', views.StationViewSet)
urlpatterns = router.urls