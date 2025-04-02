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
        actors = validated_data.pop("actors", [])
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        return movie

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if actors is not None:
            instance.actors.set(actors)

        instance.save()
        return instance
