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

