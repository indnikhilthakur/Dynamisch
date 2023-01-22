from rest_framework import serializers
from .models import *


class movie_api_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_movies_api
        fields = ['id', 'movie', 'character']


# class movies_serializers(serializers.ModelSerializer):
#     class Meta:
#                 model = model_movies_api
#                 fields = ['id', 'movie', 'character']