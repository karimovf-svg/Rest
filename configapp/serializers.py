from rest_framework import serializers
from .models import *

# class MovieSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'

class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    slug = serializers.SlugField(read_only=True)
    year = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actors.objects.all())
    genre = serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)