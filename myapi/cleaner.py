from fuzzywuzzy import process
from .models import Location

def cleaner(query):
	districts = Location.objects.all().values_list('district')
	match = [x[0][0] for x in process.extract(query, districts)]
	return match[0]