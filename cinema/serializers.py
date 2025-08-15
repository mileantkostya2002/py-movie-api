from rest_framework import serializers
from .models import Movie

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'duration', 'description']


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
