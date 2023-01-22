from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(model_movies2)
class model_movies2_admin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'character']