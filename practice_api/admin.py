from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(model_movies)

@admin.register(model_movies)
class model_movies_admin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'character']
