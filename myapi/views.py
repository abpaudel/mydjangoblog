from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer, DateSerializer, SudokuSerializer
from .cleaner import cleaner
from .date_converter import NepaliDateConverter
from .sudoku_solver import Sudoku

class LocationList(APIView):

	def get(self, request):
		locations = Location.objects.all()
		serializer = LocationSerializer(locations, many = True)
		return Response(serializer.data)

	def post(self):
		pass

class Locate(APIView):

	def get(self, request, district = None, zone = None, region = None):
		if 'district' in request.GET:
			location = get_list_or_404(Location, district = cleaner(request.GET.get('district')))
		elif 'zone' in request.GET:
			location = get_list_or_404(Location, zone = request.GET.get('zone').title())
		elif 'region' in request.GET:
			location = get_list_or_404(Location, region = request.GET.get('region').title())
		else:
			location = Location.objects.all()
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

class SudokuSolver(APIView):

	def get(self, request):
		board = request.GET.get('values')
		s = Sudoku(board)
		s = s.backtrack()
		if s is not None:
			solution = {'solution': s.allval_str()}
		else:
			solution = {'solution': 'None'}
		serializer = SudokuSerializer(solution, many = False)
		return Response(serializer.data)

