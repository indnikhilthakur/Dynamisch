from django.shortcuts import render
from .serializers import movie_api_serializer, register_user_serializers,user_kyc_info_serializers
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
import jwt

from .models import *


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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
        data = request.data
        print(data['movie'])
        serializer = movie_api_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            print(serializer.data['id'])
            id = serializer.data['id']
            encoded = jwt.encode({'id':id}, "secret", algorithm="HS256")
            print(encoded)

            return Response({'data': serializer.data, 'token': encoded})
            # return Response({'data': serializer.data})
        return Response(serializer.errors)

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

# from rest_framework_simplejwt.tokens import RefreshToken

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

class movies_auth1(viewsets.ModelViewSet):
    queryset = model_movies_api.objects.all()
    serializer_class = movie_api_serializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # refresh = RefreshToken.for_user(user)


@api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def jwt_create(request):
    
    

    if request.method == 'POST':
        # post_data = request.body.get("id")
        data_get = request.data
        print(data_get['first_name'])
        serializer = register_user_serializers(data=request.data)
        # print(serializer)
        if serializer.is_valid():

            serializer.save()
            print(serializer.data['email'])
            email = serializer.data['email']
            encoded = jwt.encode({'email':email}, "secret", algorithm="HS256")
            print(encoded)

            # serializer.data['token'] = encoded
            # serializer.save()
            # print(serializer.data['token'])
            # serializer_token.save()
            print(serializer.data)


            return Response({'data': serializer.data, 'token': encoded})
            # return Response({'data': serializer.data})
        return Response(serializer.errors)




# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImthaV9sZWVAZ21haWwuY29tIn0.Js8s2nKmyiz96DMwnEKC-lYHcPe6zoJgW4Q1rrsDBP8

@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def jwt_get(request):
    if request.method == 'GET':
        # get_data = request.headers.get('Authorization', None)
        token_data = request.headers.get('Authorization', None)
        print(token_data)
        if token_data is not None:
            decoded = jwt.decode(token_data, "secret", algorithms=["HS256"])
            print(decoded['email'])
            email_decoded = decoded['email']
            data_object = register_user.objects.get(email=email_decoded)
            print(data_object.first_name)
            serializer = register_user_serializers(data_object, many=False)
            print(serializer.data)
            return Response(serializer.data, status = status.HTTP_200_OK)
        all_data = register_user.objects.all()
        serializer = register_user_serializers(all_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        

@api_view(['PUT'])
def jwt_put(request):
    if request.method == 'PUT':
        token_data = request.headers.get('Authorization', None)
        print(token_data)
        decoded = jwt.decode(token_data, "secret", algorithms=["HS256"])
        print(decoded['email'])
        email_decoded = decoded['email']
        get_data = register_user.objects.get(email=email_decoded)
        print(get_data.first_name)
        print(request.data)
        serializer = register_user_serializers(get_data, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# @api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def get_all_data(request):
#     if request.method == 'GET':
#         # if email is not None:

#         all_data = register_user.objects.all()
#         serializer = register_user_serializers(all_data, many=True)
#         return Response(serializer.data)




# if request.method == 'PUT':
#         id = pk
#         # post_data = request.body.get("id")
#         movie = model_movies_api.objects.get(id = id)
#         serializer = movie_api_serializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_200_OK)
#         movie = model_movies_api.objects.all()
#         serializer = movie_api_serializer(movie, many = True)
#         return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)





@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_all_data(request):
    if request.method == 'GET':
        # if email is not None:

        all_data = register_user.objects.all()
        serializer = register_user_serializers(all_data, many=True)
        print(serializer.data)

        # get_data = register_user.objects.get(id = 4)
        # serializer = register_user_serializers(get_data)


        return Response(serializer.data)

    

# @api_view(['POST'])
# # @authentication_classes([JWTAuthentication])
# # @permission_classes([IsAuthenticated])
# def create_user_kyc(request):
#     if request.method == 'POST':
#         request_email = request.data["kyc_email"]
#         decoded = jwt.decode(request_email, "secret", algorithms=["HS256"])
#         print(decoded["email"])
#         # get_email = register_user.objects.get(kyc_email = decoded["email"])
#         all_register_data = register_user.objects.all()
#         # print(all_register_data[1].email)
#         for i in all_register_data:
#             # print(i.email)
#             if i.email == decoded["email"]:
#                 print(i.email)
#                 object = {
#                     "kyc_email": decoded["email"],
#                     "kyc_image": request.data["kyc_image"],
#                     "kyc_img_name": request.data["kyc_img_name"]
#                 }
#                 serializer = user_kyc_info_serializers(data=object)
#                 if serializer.is_valid():
#                     serializer.save()
#                     print(serializer.data)
#                     return Response(serializer.data)
#         return Response(serializer.errors)


@api_view(['POST'])
def create_user_kyc(request):
    if request.method == 'POST':
        print(request.data)
        print(type(request.data.get('kyc_image')))
        token_data = request.headers.get('Authorization', None)
        print(token_data)
        decoded = jwt.decode(token_data, "secret", algorithms=["HS256"])
        get_email = decoded['email']
        print(get_email)
        



        # try:
        #     register_object = register_user.objects.get(email=get_email)
        #     print(register_object.email)
        #     # if register_object.email == decoded['email']:

        #     #     serializer = user_kyc_info_serializers(data = request.data)
        #     #     serializer.data["kyc_email"] = get_email
        #     #     if serializer.is_valid():
        #     #         print(serializer.data)
        #     #         serializer.save()
        #     #         return Response(serializer.data)
        #     #     return Response(serializer.errors)

        #     # print(serializer.instance.kyc_email)
        #     serializer = user_kyc_info_serializers()
        #     # print(serializer.data['kyc_img_name'])
        #     print(serializer.data['kyc_email'])
        #     # serializer = user_kyc_info_serializers(data = request.data)
        #     serializer.data['kyc_email'] = get_email
        #     serializer.data['kyc_image'] = request.data.get('kyc_image')
        #     serializer.data['kyc_img_name'] = request.data.get('kyc_img_name')
        #     # serializer.instance
        #     if serializer.is_valid():
        #         print(serializer.data)
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors)
        # except:
        #     return Response({"error": "something went wrong"})
        register_object = register_user.objects.get(email=get_email)
        print(register_object.email)
        # if register_object.email == decoded['email']:

        #     serializer = user_kyc_info_serializers(data = request.data)
        #     serializer.data["kyc_email"] = get_email
        #     if serializer.is_valid():
        #         print(serializer.data)
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors)

        # print(serializer.instance.kyc_email)
        serializer = user_kyc_info_serializers()
        print(serializer.instance['kyc_email'])
        # print(serializer.data['kyc_img_name'])
        print(serializer.data['kyc_email'])
        # serializer = user_kyc_info_serializers(data = request.data)
        
        object = {
            'kyc_email' : get_email,
            'kyc_image' : request.data.get('kyc_image'),
            'kyc_img_name' : request.data.get('kyc_img_name')
            

        }

        serializer = user_kyc_info_serializers(data = object)

        # serializer = user_kyc_info_serializers(data.get('kyc_img_name') = request.data.get('kyc_img_name'))
        
        # print(serializer.data)
        # serializer.data['kyc_email'] = get_email
        # serializer.data['kyc_email']
        # serializer.data['kyc_image'] = request.data.get('kyc_image')
        # serializer.data['kyc_img_name'] = request.data.get('kyc_img_name')
        
        # serializer.instance
        print(serializer.data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





        # print(request.data['kyc_email'])
        # request.data["kyc_email"] = get_email
        # # data_get = request.data
        # # print(data_get["kyc_img_name"])
        # # print(data_get)
        # print(request.data['kyc_email'])
        # serializer = user_kyc_info_serializers(data=request.data)
        # # print(serializer.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     print(serializer.data)
        #     return Response(serializer.data)
        # return Response(serializer.errors)

@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def get_user_kyc(request):

    if request.method == 'GET':
        all_data = user_kyc_info.objects.all()
        serializer = user_kyc_info_serializers(all_data, many=True)
        print(serializer.data)
        print(serializer.data[1]['kyc_image'])
        return Response(serializer.data)





@api_view(['GET', 'POST', 'PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def jwt_poc(request):
    if request.method == 'POST':
        # post_data = request.body.get("id")
        data_get = request.data
        print(get_data)
        print(data_get['first_name'])
        serializer = register_user_serializers(data=request.data)
        # print(serializer)
        if serializer.is_valid():

            serializer.save()
            print(serializer.data['email'])
            email = serializer.data['email']
            encoded = jwt.encode({'email':email}, "secret", algorithm="HS256")
            print(encoded)

            # serializer.data['token'] = encoded
            # serializer.save()
            # print(serializer.data['token'])
            # serializer_token.save()
            print(serializer.data)


            return Response({'data': serializer.data, 'token': encoded})
            # return Response({'data': serializer.data})
        return Response(serializer.errors)

    
    if request.method == 'GET':
        # get_data = request.headers.get('Authorization', None)
        token_data = request.headers.get('Authorization', None)
        print(token_data)
        decoded = jwt.decode(token_data, "secret", algorithms=["HS256"])
        print(decoded['email'])
        email_decoded = decoded['email']
        data_object = register_user.objects.get(email=email_decoded)
        print(data_object.first_name)
        serializer = register_user_serializers(data_object, many=False)
        print(serializer.data)
        return Response(serializer.data)

    # if request.method == 'GET':
    #     # get_data = request.headers.get('Authorization', None)
    #     token_data = request.headers.get('Authorization', None)
    #     print(token_data)
    #     if token_data is not None:
    #         decoded = jwt.decode(token_data, "secret", algorithms=["HS256"])
    #         print(decoded['email'])
    #         email_decoded = decoded['email']
    #         data_object = register_user.objects.get(email=email_decoded)
    #         print(data_object.first_name)
    #         serializer = register_user_serializers(data_object, many=False)
    #         print(serializer.data)
    #         return Response(serializer.data, status = status.HTTP_200_OK)
    #     all_data = register_user.objects.all()
    #     serializer = register_user_serializers(all_data, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        token_data = request.headers.get('Authorization', None)
        print(token_data)
        decoded = jwt.decode(token_data, "secret", algorithms=["HS256"])
        print(decoded['email'])
        email_decoded = decoded['email']
        get_data = register_user.objects.get(email=email_decoded)
        print(get_data.first_name)
        print(request.data)
        serializer = register_user_serializers(get_data, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


        
    