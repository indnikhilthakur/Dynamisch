from django.contrib import admin
from .models import *


@admin.register(model_movies3)
class model_movies3_admin(admin.ModelAdmin):
    list_diaplay = ['id', 'movie', 'character']