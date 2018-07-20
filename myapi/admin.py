from django.contrib import admin
from .models import Location
from .models import ChildGrantDate


class LocationDetailAdmin(admin.ModelAdmin):
	list_display = ('district', 'zone', 'region')
	list_filter = ('district', 'zone', 'region')
	search_fields = ['district', 'zone', 'region']

class ChildGrantDateDetailAdmin(admin.ModelAdmin):
	list_display = ('address_group', 'dist_date_np', 'dist_date_en', 'final_confirmation', 'last_updated_date')
	list_filter = ('address_group', 'dist_date_np', 'dist_date_en', 'final_confirmation', 'last_updated_date')
	search_fields = ['address_group', 'dist_date_np', 'dist_date_en', 'final_confirmation', 'last_updated_date']

admin.site.register(Location, LocationDetailAdmin)
admin.site.register(ChildGrantDate, ChildGrantDateDetailAdmin)