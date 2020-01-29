from rest_framework import serializers
from .models import People, Film


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    #characters = PeopleSerializer(read_only=True, many=True)

    class Meta:
        model = Film
        fields = '__all__'
