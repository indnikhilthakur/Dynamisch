from django.shortcuts import render
from django.http import JsonResponse 
from .models import *
from .serializers import movies_serializers
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

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from django.contrib.auth.models import User
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

# Create your views here.
@api_view(['GET', 'POST'])

def all_movies(request):
    # select all_movies
    # serialize them
    # return json
    print("rendering .....")
    
    if request.method == 'GET':

        movies = model_movies.objects.all()
        serializer = movies_serializers(movies, many=True)
        print(type(serializer))
        print(serializer.data)
        
        # print(serializer)
        # return JsonResponse(serializer.data, safe=False)
        # return JSONRenderer().render("rendering .....")
        
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type='application/json')

        return JsonResponse({"movies":serializer.data})

    if request.method == 'POST':
        
        serializer = movies_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'put', 'DELETE'])
def movie_data(request, id):
    try:
        get_data = model_movies.objects.get(pk = id)
        print(get_data.pk)
    except model_movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = movies_serializers(get_data)
        return Response(serializer.data)
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass


# serialization
def movie_d(request):
    movie = model_movies.objects.all()
    
     # movie = model_movies.objects.get(pk = 3)
    # serializer = movies_serializers(movie)
    
    serializer = movies_serializers(movie, many = True)
    json_data = JSONRenderer().render(serializer.data)
    
    # json_data = JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params= = none, **kwargs)
    # json_data = JsonResponse(serializer.data, safe = False)
    # return json_data
     
    return HttpResponse(json_data, content_type='application/json')

# single entry from entry
def get_movie_d(request, id):
    movie = model_movies.objects.get(id = id)
    # quesry set
    print(movie.character)
    print(type(movie))
    serializer = movies_serializers(movie)
    # python dictionary
    print(serializer.data)
    print(type(serializer.data))
    json_data = JSONRenderer().render(serializer.data)
    # json output
    print(json_data)
    print(type(json_data))
    return HttpResponse(json_data, content_type = 'application/json')

# deserialization
@csrf_exempt
def create_movie(request):
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

        serializer = movies_serializers(data=python_data)
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


# crud operations using rest framework creating rest_api 

@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = movies_serializers(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type ='application/josn')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='application/josn')


@csrf_exempt
def put_data(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        movie = model_movies.objects.get(id=id)
        serializer = movies_serializers(movie, data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data_updated'}
            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type= 'application/json')

# getting data from data base and sending to client
@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            movie = model_movies.objects.get(id=id)
            serializer = movies_serializers(movie)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type= 'application/json')
        movie = model_movies.objects.all()
        serializer = movies_serializers(movie, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = movies_serializers(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type ='application/josn')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='application/josn')

    # partial update
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        movie = model_movies.objects.get(id=id)
        serializer = movies_serializers(movie, data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data_updated'}
            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type= 'application/json')

    # complete update
    # if request.method == 'PUT':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id')
    #     movie = model_movies.objects.get(id=id)
    #     serializer = movies_serializers(movie, data = python_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg':'data_updated'}
    #         json_data = JSONRenderer().render(res)

    #         return HttpResponse(json_data, content_type= 'application/json')
    #     json_data = JSONRenderer().render(serializer.errors)

    #     return HttpResponse(json_data, content_type= 'application/json')

    if request.method == "DELETE":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        movie = model_movies.objects.get(id= id)
        movie.delete()
        res ={'msg' : 'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'applicattion/json')


# generic views and model mixin
# class movie_list(GenericAPIView, ListModelMixin):
#     queryset = model_movies.objects.all()
#     serializer_class = movies_serializers
    

#     def get





class movie_list(generics.ListCreateAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers
    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        print("rendering .....")
        print(queryset)
        serializer = movies_serializers(queryset, many=True)
        return Response(serializer.data)



# use of class in views for creating api
@method_decorator(csrf_exempt, name='dispatch')
class movie_api(View):
    def get(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            movie = model_movies.objects.get(id=id)
            serializer = movies_serializers(movie)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type= 'application/json')
        movie = model_movies.objects.all()
        serializer = movies_serializers(movie, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = movies_serializers(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type ='application/josn')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='application/josn')

    def put(self, request, *argss, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        movie = model_movies.objects.get(id=id)
        serializer = movies_serializers(movie, data = python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data_updated'}
            json_data = JSONRenderer().render(res)

            return HttpResponse(json_data, content_type= 'application/json')
        json_data = JSONRenderer().render(serializer.errors)

        return HttpResponse(json_data, content_type= 'application/json')

    def delete(sef, request, *args, **kwargs):
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        movie = model_movies.objects.get(id= id)
        movie.delete()
        res ={'msg' : 'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'applicattion/json')



# decorators for rest api rest framework @API_Views
from django.shortcuts import render 
from rest_framework.decorators import api_view

@api_view()
def api_msg(request):
    return Response({'msg': 'rendering.....'})

# @api_view(['GET'])
# def api_msg(request):
#     return Response({'msg': 'rendering.....'})

@api_view(['POST'])
def post_msg(request):
    if request.method == "POST":
        print(request.data)
        return Response({'msg': 'rendering.....', "object": request.data})


@api_view(['GET', 'POST'])
def get_post_msg(request):
    if request.method == 'GET':
        movies = model_movies.objects.all()
        serializer = movies_serializers(movies, many=True)
        print(serializer.data)
        return Response({"movies":serializer.data})
    
    if request.method == "POST":
        print(request.data)
        serializer = movies_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'msg': 'rendering.....', "object": serializer.data})


@api_view(['GET'])
def crud(request, id = None):
    # id  = request.data
    # print("this is data " + id)
    if request.method == 'GET':
        id = request.data.get(id)
        print(request.data)
        if id is not None:
            print(id)
            movie_d = model_movies.objects.get(id = id)
            serializer = movies_serializers(movie_d)
            return Response({'msg': 'single entry rendering.....', 'movie':serializer.data})
        movie_data = model_movies.objects.all()
        serializer = movies_serializers(movie_data, many = True)
        return Response({'msg': 'all data rendering.....', 'movie':serializer.data})

# concrete views classes
class movies_list_class(generics.ListAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class movie_create_class(generics.CreateAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class movie_retrieve_class(generics.RetrieveAPIView):
    queryset = model_movies.objects.all()
    srializer_class = movies_serializers

class movie_update_class(generics.UpdateAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class movie_destroy_class(generics.DestroyAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers 

class movie_list_create_class(generics.ListCreateAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class movie_retrieve_update_class(generics.RetrieveUpdateAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class movie_retrieve_destroy_class(generics.RetrieveDestroyAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class movie_retrieve_update_destroy_class(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class concreate_generic_views_class_list_create(generics.ListCreateAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

class concreate_generic_views_class_retrieve_update_destroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_movies.objects.all()
    serializer_class = movies_serializers

# get all data
# method 1

def movie_d(request):
    movie = model_movies.objects.all()
    
     # movie = model_movies.objects.get(pk = 3)
    # serializer = movies_serializers(movie)
    
    serializer = movies_serializers(movie, many = True)
    json_data = JSONRenderer().render(serializer.data)
    
    # json_data = JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params= = none, **kwargs)
    # json_data = JsonResponse(serializer.data, safe = False)
    # return json_data
     
    return HttpResponse(json_data, content_type='application/json')

def get_all_data(request):
    movie = model_movies.objects.all()
    serializer = movies_serializers(movie, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
