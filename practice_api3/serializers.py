from rest_framework import serializers
from .models import *

class movies3_serializers(serializers.ModelSerializer):
    class Meta:
        model = model_movies3
        fields = ["id", "movie", "character"]