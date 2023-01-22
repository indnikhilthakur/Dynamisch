from rest_framework import serializers
from .models import *

# validators
def start_with_m(value):
    if value[0].lower() != "m":
        raise serializers.ValidationError("error occured character name isen't start with m")
    return value

class movies2_serializers(serializers.Serializer):
    id = serializers.IntegerField()
    movie = serializers.CharField(max_length = 100, read_only = True)
    character = serializers.CharField(max_length = 100, validators = [start_with_m])

    def create(self, validate_data):
                return model_movies2.objects.create(**validate_data)

    def update(self, instance, validate_data):
                print(instance.name)
                print(instance.movie)
                instance.movie = validate_data.get('movie', instance.movie)
                print(instance.movie)
                instance.character = validate_data.get('character', instance.character)
                instance.save()
                return instance

    # field level validation
    def validate_movie(self, value):
                if len(value) < 2 :
                        raise serializers.ValidationError("validation strikes")
                return value

    # object level validation
    def validate(self, data):
        get_movie = data.get('movie')
        print(get_movie)
        print(get_movie.lower())
        print(type(get_movie))
        get_character = data.get('character')
        if get_movie.lower() == "avengers: infinity war" and get_character.lower() == "hulk":
            raise serializers.ValidationError("all laters must be in lower case")
        return data
