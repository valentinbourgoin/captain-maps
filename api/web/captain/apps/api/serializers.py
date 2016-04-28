from rest_framework import serializers

from captain.apps.core.models import Station

class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('uic', 'name', 'latitude', 'longitude')
