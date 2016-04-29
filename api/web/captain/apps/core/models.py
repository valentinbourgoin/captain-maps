from django.db import models

class Station(models.Model): 
	"""
	Station model
	"""
	uic       = models.CharField(max_length=7)
	name      = models.CharField(max_length=255)
	latitude  = models.FloatField()
	longitude = models.FloatField()
