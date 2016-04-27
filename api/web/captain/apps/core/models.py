from django.db import models

### 
# Station model 
###
class Station(models.Model): 
	uic       = models.CharField(max_length=7)
	name      = models.CharField(max_length=255)
	latitude  = models.FloatField()
	longitude = models.FloatField()
