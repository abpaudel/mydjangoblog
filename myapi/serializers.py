from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Location
		fields = ('district', 'zone', 'region')

class DateSerializer(serializers.Serializer):

	date_type = serializers.CharField(max_length=2)
	date = serializers.CharField(max_length=10)
	year = serializers.IntegerField()
	month = serializers.IntegerField()
	day = serializers.IntegerField()

class SudokuSerializer(serializers.Serializer):

	solution = serializers.CharField(max_length=81)