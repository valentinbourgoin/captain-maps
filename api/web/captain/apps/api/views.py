from django.core import serializers
from django.http import HttpResponse

from captain.apps.core.models import Station

LIMIT = 20

def stations(request):
	stations = Station.objects.all()

	# Get parameters
	lat_min = request.GET.get('lat_min')
	lat_max = request.GET.get('lat_max')
	lg_min = request.GET.get('lg_min')
	lg_max = request.GET.get('lg_max')
	if(lat_min and lat_max, lg_min, lg_max):
		stations = stations.filter(latitude__range=(lat_min, lat_max), longitude__range=(lg_min, lg_max))

	stations = stations[:LIMIT]

	# Serialize models and return data
	data = serializers.serialize('json', stations)
	return HttpResponse(data, content_type="application/json")