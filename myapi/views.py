from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer, DateSerializer
from .cleaner import cleaner
from .date_converter import NepaliDateConverter

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

	def post(self):
		pass

class AD_BS(APIView):

	def get(self, request):
		ad = request.GET.get('date')
		dc = NepaliDateConverter()
		ad = tuple(map(int, ad.split('-')))
		bs = dc.ad2bs(ad)
		datestr = '-'.join([str(x).zfill(2) for x in bs])
		date = {'date_type': 'BS', 'date': datestr, 'year': bs[0], 'month': bs[1], 'day': bs[2]}
		serializer = DateSerializer(date, many = False)
		return Response(serializer.data)

	def post(self):
		pass

class BS_AD(APIView):

	def get(self, request):
		bs = request.GET.get('date')
		dc = NepaliDateConverter()
		bs = tuple(map(int, bs.split('-')))
		ad = dc.bs2ad(bs)
		datestr = '-'.join([str(x).zfill(2) for x in ad])
		date = {'date_type': 'AD', 'date': datestr, 'year': ad[0], 'month': ad[1], 'day': ad[2]}
		serializer = DateSerializer(date, many = False)
		return Response(serializer.data)

	def post(self):
		pass
