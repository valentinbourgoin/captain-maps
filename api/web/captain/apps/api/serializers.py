from rest_framework import serializers

from captain.apps.core.models import Station

class StationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Station serializer
    Define station field to JSON to use in JSON response
    """
    class Meta:
        model = Station
        fields = ('uic', 'name', 'latitude', 'longitude')
