from django.shortcuts import render
from django.http import JsonResponse 
from .models import *
from .serializers import movies2_serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
# csrf token for serializers
from django.views.decorators.csrf import csrf_exempt
# use of class in views.py for creating api
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

def get_movies2(request):
    movie_data = model_movies2.objects.all()

    serializer = movies2_serializers(movie_data, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

# @csrf_exempt
def create_movie2(request):
    if request.method == "POST":
        json_data = request.body
        # print(json_data)
        # print(type(json_data))
        # b'{"movie": "movie4", "character": "c4"}'
        # <class 'bytes'>
        
        stream = io.BytesIO(json_data)
        # print(stream)
        # print(type(stream))
        # <_io.BytesIO object at 0x00000212E15DF1D0>
        # <class '_io.BytesIO'>
       
        python_data = JSONParser().parse(stream)
        # print(python_data)
        # print(type(python_data))
        # {'movie': 'movie3', 'character': 'c3'}
        # <class 'dict'>

        serializer = movies2_serializers(data=python_data)
        # print(ser ializer)
        # print(type(serializer))
        # movies_serializers(data={'movie': 'movie4', 'character': 'c4'}):
        # id = IntegerField(label='ID', read_only=True)
        # movie = CharField(max_length=100)
        # character = CharField(max_length=100)
        # <class 'practice_api.serializers.movies_serializers'>

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data_created'}
            json_data =JSONRenderer().render(res['msg'])
            print(json_data)
            print(type(json_data))
            # movies_serializers(data={'movie': 'movie5', 'character': 'c5'}):
            # id = IntegerField(label='ID', read_only=True)
            # movie = CharField(max_length=100)
            # character = CharField(max_length=100)
            # <class 'practice_api.serializers.movies_serializers'>
            # b'{"msg":"data_created"}'
            # <class 'bytes'>
            
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def put_movies2(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        movie = model_movies2.objects.get(id=id)
        serializer = movies2_serializers(movie, data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data_updated'}
            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type= 'application/json')




    


