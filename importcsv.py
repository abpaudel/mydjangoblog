from myapi.models import Location
import csv
data = csv.reader(open('zones_with_districts.csv'), delimiter=',')
for row in data:
	impdata = Location()
	impdata.district = row[0]
	impdata.zone = row[1]
	impdata.region = row[2]
	impdata.save()
