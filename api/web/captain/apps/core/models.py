from django.contrib.gis.db import models

### 
# Station model 
###
class Station(models.Model): 
	name         = models.CharField(max_length=255)
	coordinates  = models.PointField()

	objects = models.GeoManager()

