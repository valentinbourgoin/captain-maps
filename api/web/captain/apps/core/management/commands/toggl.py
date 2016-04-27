import requests

from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from captain.apps.core.models import Station

### 
# Command to sync all stations data from CSV file
###
class Command(BaseCommand):
	help = "Get stations data"

	def handle(self, *args, **options): 
		
		# @todo

		self.stdout.write("-----")
		self.stdout.write("Stations import done!")
		self.stdout.write("-----")
