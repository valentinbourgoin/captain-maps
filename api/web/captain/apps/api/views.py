#from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from captain.apps.core.models import Station
from . import serializers 

# Default limit 
LIMIT = 30

class StationViewSet(viewsets.ViewSet):
    """
    Class used to serve station related resources
    Django REST Framework subclass
    """
    queryset = Station.objects.all()

    def list(self, request):
        """
        List GET resource
        """
        # Get URL parameters
        lat_min = request.GET.get('lat_min')
        lat_max = request.GET.get('lat_max')
        lg_min = request.GET.get('lg_min')
        lg_max = request.GET.get('lg_max')
        
        # Process query
        if(lat_min and lat_max, lg_min, lg_max):
            stations = self.queryset.filter(latitude__range=(lat_min, lat_max), longitude__range=(lg_min, lg_max))
        stations = stations[:LIMIT]

        # Serialize data and return response
        serializer = serializers.StationSerializer(stations, many=True)
        return Response(serializer.data)