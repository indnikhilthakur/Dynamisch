from rest_framework import serializers
from .models import *

# method 1
class movies_serializers(serializers.ModelSerializer):
        #  method 1 use of read only for single field in model serializers
        # movie = serializers.CharField(read_only = True)
        
        # validators
        # def start_with_m(value):
        #         if value[0].lower() != "m":
        #                 raise serializers.ValidationError("error occured character name isen't start with m")
        #         return value
        # character = serializers.CharField(max_length = 100, validators = [start_with_m])

        class Meta:
                model = model_movies
                fields = ['id', 'movie', 'character']

                # method 2 use of read only  for multiple fields in model serializers
                # read_only_fields = ['character']
                
                # method 3 use of read only method for single and multiple fields with differnt methods in model serializers.
                # extra_kwargs = {'character':{'read_only':True}}


        # field level validation
        # def validate_movie(self, value):
        #         if len(value) < 2 :
        #                 raise serializers.ValidationError("validation strikes")
        #         return value
        

        # object level validation
        def validate(self, data):
                get_movie = data.get('movie')
                # print(get_movie)
                # print(get_movie.lower())
                # print(type(get_movie))
                get_character = data.get('character')
                if get_movie.lower() == "avengers: infinity war" and get_character.lower() == "hulk":
                        raise serializers.ValidationError("this entry is already exists")
                return data


        # def create(self, validate_data):
        #         return model_movies.objects.create(**validate_data)

        # def update(self, instance, validate_data):
        #         print(instance.name)
        #         print(instance.movie)
        #         instance.movie = validate_data.get('movie', instance.movie)
        #         print(instance.movie)
        #         instance.character = validate_data.get('character', instance.character)
        #         instance.save()
        #         return instance
        
        # def validate_movie(self, value):
        #         if len(value) >= 2 :
        #                 raise serializers.ValidationError("movie name should be more than 2 characters")
        #         return value


# # method 2
# class movies_serializers(serializers.Serializer):
#    id = serializers.IntegerField()
#    movie = serializers.CharField(max_length=100)
#    character = serializers.CharField(max_legth=100)



# # validators
# def start_with_m(value):
#     if value[0].lower() != "m":
#         raise serializers.ValidationError("error occured character name isen't start with m")
#     return value

# class movies_serializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     movie = serializers.CharField(max_length = 100, read_only = True)
#     character = serializers.CharField(max_length = 100, validators = [start_with_m])

#     def create(self, validate_data):
#                 return model_movies.objects.create(**validate_data)

#     def update(self, instance, validate_data):
#                 print(instance.name)
#                 print(instance.movie)
#                 instance.movie = validate_data.get('movie', instance.movie)
#                 print(instance.movie)
#                 instance.character = validate_data.get('character', instance.character)
#                 instance.save()
#                 return instance

#     # field level validation
#     def validate_movie(self, value):
#                 if len(value) < 2 :
#                         raise serializers.ValidationError("validation strikes")
#                 return value

#     # object level validation
#     def validate(self, data):
#         get_movie = data.get('movie')
#         print(get_movie)
#         print(get_movie.lower())
#         print(type(get_movie))
#         get_character = data.get('character')
#         if get_movie.lower() == "avengers: infinity war" and get_character.lower() == "hulk":
#             raise serializers.ValidationError("all laters must be in lower case")
#         return data