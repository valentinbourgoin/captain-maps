# encoding=utf8  
import sys, os, csv

from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from captain.apps.core.models import Station
from captain import settings

reload(sys)
sys.setdefaultencoding('utf8')

### 
# Command to sync all stations data from CSV file
###
class Command(BaseCommand):
	help = "Get stations data"
	filename = os.path.join(settings.PROJECT_DIR, '../stations/stations.csv')

	def handle(self, *args, **options): 
		
		self.stdout.write("Opening %s..." % self.filename)
		f = open(self.filename)
		reader = csv.reader(f, delimiter=';')
		next(reader) # Exclude first line
		for row in reader:
			try: 
				station = Station.objects.get(uic=row[3])
			except ObjectDoesNotExist: 
				station = Station()
			try: 
				station.uic       = row[3]
				station.name      = row[1]
				station.latitude  = float(row[5])
				station.longitude = float(row[6])
				station.save()
				self.stdout.write("Saving %s" % station.name)
			except: 
				self.stdout.write("Error saving %s" % station.name)


		f.close()

		self.stdout.write("-----")
		self.stdout.write("Stations import done!")
		self.stdout.write("-----")
