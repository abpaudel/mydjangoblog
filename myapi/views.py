from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer
from .cleaner import cleaner

class LocationList(APIView):

	def get(self, request):
		locations = Location.objects.all()
		serializer = LocationSerializer(locations, many = True)
		return Response(serializer.data)

	def post(self):
		pass

class LocationSpecific(APIView):

	def get(self, request, district = None, zone = None, region = None):
		if district:
			location = get_list_or_404(Location, district = cleaner(district))
		elif zone:
			location = get_list_or_404(Location, zone = zone.title())
		elif region:
			location = get_list_or_404(Location, region = region.title())
		else:
			pass
		serializer = LocationSerializer(location, many = True)
		return Response(serializer.data)