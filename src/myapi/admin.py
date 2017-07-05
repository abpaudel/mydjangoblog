from django.contrib import admin
from .models import Location

class LocationDetailAdmin(admin.ModelAdmin):
	list_display = ('district', 'zone', 'region')
	list_filter = ('district', 'zone', 'region')
	search_fields = ['district', 'zone', 'region']

admin.site.register(Location, LocationDetailAdmin)