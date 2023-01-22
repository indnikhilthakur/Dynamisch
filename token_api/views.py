from django.shortcuts import render
from .serializers import movie_api_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView, authentication_classes, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
# from rest_framework.permissions import IsAuthenticated
# from .custom_permissions import custom_get_permission
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def decorators_movies_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        # id = request.data.get('id')
        if id is not None:
            movie = model_movies_api.objects.get(id = id)
            serializer = movie_api_serializer(movie)
            return Response(serializer.data)
        movie = model_movies_api.objects.all()
        serializer = movie_api_serializer(movie, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        # post_data = request.body.get("id")
        serializer = movie_api_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return(serializer.errors)

    if request.method == 'PUT':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies_api.objects.get(id = id)
        serializer = movie_api_serializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_200_OK)
        movie = model_movies_api.objects.all()
        serializer = movie_api_serializer(movie, many = True)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)
        
    if request.method == 'PATCH':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies_api.objects.get(id = id)
        serializer = movie_api_serializer(movie, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_200_OK)
        movie = model_movies_api.objects.all()
        serializer = movie_api_serializer(movie, many = True)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)

    if request.method == 'DELETE':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies_api.objects.get(id = id)
        movie.delete()
        return Response({'msg':'rendering.....'}, status = status.HTTP_200_OK)

# jwt token

# 

class movie_generic_api(ListCreateAPIView):
    queryset = model_movies_api.objects.all()
    serializer_class = movie_api_serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   

class movies_auth(viewsets.ModelViewSet):
    queryset = model_movies_api.objects.all()
    serializer_class = movie_api_serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoObjectPermissions]
    # permission_classes = [custom_get_permission]

class movies_auth1(viewsets.ModelViewSet):
    queryset = model_movies_api.objects.all()
    serializer_class = movie_api_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]