from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(model_movies_api)
class model_movies_appi_admin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'character']


@admin.register(register_user)
class register_user_admin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_no', 'password', 'first_name', 'last_name', 'address']

@admin.register(user_kyc_info)
class user_kyc_info(admin.ModelAdmin):
    list_display = ['id', 'kyc_email', 'kyc_image', 'kyc_img_name']