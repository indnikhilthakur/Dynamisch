from rest_framework import serializers
from .models import *


class movie_api_serializer(serializers.ModelSerializer):
    class Meta:
        model = model_movies_api
        fields = ['id', 'movie', 'character']


class register_user_serializers(serializers.ModelSerializer):
    class Meta:
        model = register_user
        fields = ['id', 'first_name', 'last_name', 'phone_no', 'email', 'address', 'token']


class user_kyc_info_serializers(serializers.ModelSerializer):
    class Meta:
        model = user_kyc_info
        fields = ['id', 'kyc_email', 'kyc_image', 'kyc_img_name']

    # def create(self, instance, **kwargs):
# custom serializer for 2 different models(register_user and user_kyc_info)
class user_update_kyc_serializer(serializers.ModelSerializer):
    class Meta:
        model = register_user, user_kyc_info
        fields = ['id', 'email', 'first_name', 'last_name', 'address', 'kyc_image', 'kyc_img_name']