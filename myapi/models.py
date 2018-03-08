from django.db import models

class Location(models.Model):
	district = models.CharField(max_length=20)
	zone = models.CharField(max_length=20)
	region = models.CharField(max_length=30)
	
	def __self__(self):
		return self.district + ', ' + self.zone + ', ' + self.region
		