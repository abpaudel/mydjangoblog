from django.db import models

class Location(models.Model):
	district = models.CharField(max_length=20)
	zone = models.CharField(max_length=20)
	region = models.CharField(max_length=30)
	
	def __self__(self):
		return self.district + ', ' + self.zone + ', ' + self.region

class ChildGrantDate(models.Model):
	address_group = models.CharField(max_length=50, primary_key=True, verbose_name='Location')
	dist_date_np = models.CharField(max_length=20, null=True, blank=True, verbose_name='Distribution Date (NP)')
	dist_date_en = models.CharField(max_length=20, null=True, blank=True, verbose_name='Distribution Date (EN)')
	final_confirmation = models.CharField(max_length=20, null=True, blank=True, verbose_name='Final Confirmation')
	last_updated_date = models.DateField(null=True, verbose_name='Last Updated On')
	
	def __self__(self):
		return self.address_group + ': ' + self.dist_date_np
