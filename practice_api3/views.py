from django.shortcuts import render
from .serializers import movies3_serializers
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
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions
# from rest_framework.permissions import IsAuthenticated
from .custom_permissions import custom_get_permission

from .models import *

# get method 
# method 1
def get_data_movies(request):
    movies = model_movies3.objects.all()
    serializer = movies3_serializers(movies, many = True)
    
    # with use of JSONRenderer().render() and HTTPResponse()
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    
    # JSONResponse
    return JsonResponse(serializer.data, safe=False, status = status.HTTP_200_OK)

def get_data_movie_id(request, pk):
    movie = model_movies3.objects.get(id = pk)
    # getting quearyset
    serializer = movies3_serializers(movie)
    # movie as queyset converted to python data as serializer 
    json_data = JSONRenderer().render(serializer.data)
    # as serializer is python dictionary format converting to json format to send this data to brawser
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data, data = False)


# method 2
@api_view(['GET'])
def get_all_views(request):
    movie = model_movies3.objects.all()
    serializer = movies3_serializers(movie, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['GET'])
def get_id_view(request, pk):
    movie = model_movies3.objects.get(id = pk)
    serializer = movies3_serializers(movie)
    return Response(serializer.data, status = status.HTTP_200_OK)

# method 3
class movies_list_class(ListAPIView):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers

class movie_retrieve_class(RetrieveAPIView):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers

class concreate_generic_views_class_retrieve_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers


# def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)



# create api view

# create api
# method 1
@csrf_exempt
def create_api(request):
    # if request.method == 'POST':
    post_data_bytes = request.body
    stream = io.BytesIO(post_data_bytes)
    python_data = JSONParser().parse(stream)
    serializer = movies3_serializers(data = python_data)
    if serializer.is_valid():
        serializer.save()
        res = {"msg": "entry is valid"}
        json_data = JSONRenderer().render(res["msg"])
        return HttpResponse(json_data, content_type = "application/json")
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type = "application/json")


# method 2
@api_view(['GET', 'POST'])
def create_api_post(request):
    if request.method == 'GET':
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    if request.method == 'POST':
        serializer = movies3_serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_201_CREATED)

# method 3
class create_api_class(CreateAPIView):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers

class create_api_generic_lc(ListCreateAPIView):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers


class create_list_class(generics.ListCreateAPIView):
    queryset = model_movies3.objects.all()                                                                                                                                     
    serializer_class = movies3_serializers  

# generic views and model mixins with serializers.
class generic_mixin_movie_data_list_create(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers
    def get(self, request, *args, **kwargs):
        # if request.id == 1:
        #     get_instance = model_movies3.objects.get(id = 1)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class generic_mixin_movie_retrieve_update_delete(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args,**kwargs)


# APIView class CRUD operatios
class api_view_class(APIView):
    def get(self, request, pk = None, format = None):
        # id  = request.data.get("id")
        id = request.data.get("id")
        pk = id
        if pk is not None:
            movie = model_movies3.objects.get(id = pk)
            serializer = movies3_serializers(movie)
            return Response({"msg" : "rendering.....", "object" : serializer.data}) 
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response({"msg" : "rendering....", "object" : serializer.data})

    def post(self, request, format = None):
        # new_movie = request.body
        # steram = io.BytesIO(new_movie)
        # python_data = JSONParser().parse(steram)
        # serializer = movies3_serializers(python_data)
        # return Response({"object": serializer.data})
        
        # # serializer = movies3_serializers(data = request.data)
        # # if serializer.is_valid():
        # #     serializer.save()

        # # return Response({"object": serializer.data})

        serializer = movies3_serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors)

    def put(self, request, pk, format = None):
        id = pk
        json_data = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(json_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id = pk
        json_data = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(json_data, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        id = pk 
        json_data = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(json_data)
        serializer.delete()
        return Response({"msg": "given data is deleted"}, status = status.HTTP_204_NO_CONTENT)




# api view get function 
def get_data_crud(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(json_data)
        id = python_data.get('id', None)
        print(id)
        # id = request.data.get('id')
        print(id)
        if id is not None :
            print("rendering.....")
            movie = model_movies3.objects.get(id = id)
            serializer = movies3_serializers(movie)
            # return Response({"object" : serializer.data})
            # json_data = JSONRenderer().render(res["msg"])
            # return HttpResponse(json_data, content_type = "application/json")
            return JsonResponse(serializer.data, safe = False)
        print("rendering......!")
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)

        # return Response({"msg": "rendering.....", "object" : serializer.data})

        # return JsonResponse(serializer.data, safe = False)

        # res = {"msg" : "this is working"}
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = "application/json")


# @api_view CRUD operations
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def get_api_view_def(request, pk=None):
    if request.method == 'GET':
        id = pk
        # id = request.data.get('id')
        if id is not None:
            movie = model_movies3.objects.get(id = id)
            print(movie.character)
            movie_data = json.dumps()
            serializer = movies3_serializers(movie)
            return Response(serializer.data)
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        # post_data = request.body.get("id")
        post_data = request.data
        serializer = movies3_serializers(post_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return(serializer.errors)

    if request.method == 'PUT':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_200_OK)
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)
        
    if request.method == 'PATCH':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(movie, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_200_OK)
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)

    if request.method == 'DELETE':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(movie)
        serializer.delete()
        return Response({'msg':'rendering.....'}, status = status.HTTP_200_OK)

# viewsets
class movie_viewset_class(viewsets.ViewSet):
    def list(self, request):
        print("--------------list-----------------")
        print("basename", self.basename)
        print("action", self.action)
        print("detail", self.detail)
        print("suffix", self.suffix)
        print("name", self.name)
        print("description", self.description)
        movie_data = model_movies3.objects.all()
        serializer = movies3_serializers(movie_data, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        print("--------------retrieve-----------------")
        print("basename", self.basename)
        print("action", self.action)
        print("detail", self.detail)
        print("suffix", self.suffix)
        print("name", self.name)
        print("description", self.description)
        id = pk
        if id is not None:
            movie_data = model_movies3.objects.get(pk = id)
            serializer = movies3_serializers(movie_data)
            return Response(serializer.data)

    def create(self, request):
        print("--------------create-----------------")
        print("basename", self.basename)
        print("action", self.action)
        print("detail", self.detail)
        print("suffix", self.suffix)
        print("name", self.name)
        print("description", self.description)
        serializer = movies3_serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "new instance was created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        print("--------------update-----------------")
        print("basename", self.basename)
        print("action", self.action)
        print("detail", self.detail)
        print("suffix", self.suffix)
        print("name", self.name)
        print("description", self.description)
        id = pk
        movie_data = model_movies3.objects.get(id = pk)
        serializer = movies3_serializers(movie_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "data is updated"})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        print("--------------delete-----------------")
        print("basename", self.basename)
        print("action", self.action)
        print("detail", self.detail)
        print("suffix", self.suffix)
        print("name", self.name)
        print("description", self.description)
        id = pk
        movie_data = model_movies3.objects.get(id = pk)
        movie_data.delete()
        return Response({"msg" : "data deleted"})

# modelviewset 
class movie_model_viewset(viewsets.ModelViewSet):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers

# readonlymodelviewset
class movie_readonlymodelviewset(viewsets.ReadOnlyModelViewSet):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers


# crud with json
def json_crud(request):
    data = model_movies3.objects.all()
    print(data)
    list_data = list(data)
    print(list_data)
    json_data = json.dumps(data)
    print(json_data)
    # json_loads = json.loads(json_data) 
    # print(json_loads)
    # return HttpResponse(json_loads, safe = False)


@api_view(['GET'])
def movie_data(request, id):
    try:
        get_data = model_movies3.objects.get(pk = id)
        print(get_data)
        stream = io.BytesIO(get_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        return Response(python_data)
    except model_movies3.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # if request.method == "GET":
    #     serializer = movies_serializers(get_data)
    #     return Response(serializer.data)
    # elif request.method == "PUT":
    #     pass
    # elif request.method == "DELETE":
    #     pass


# method 1 without serializers creating api for CRUD operations
@csrf_exempt
def without_serializer(request, id):
    if request.method == 'PUT':
        # # id = model_movies3.objects.get(id = id)

        # method 1
        # post_data = request.body
        # stream = io.BytesIO(post_data)
        # python_data = JSONParser().parse(stream)
        # print(python_data)
        # get_data_add = model_movies3.objects.filter(id = id).update(id = id, movie = python_data['movie'], character = python_data['character'])
        # # get_data_add.movie = python_data['movie']
        # # get_data_add.save()

        # json_data = JSONRenderer().render(python_data)
        # return HttpResponse(json_data, content_type = "application/json")

        # method 2 

        post_data = request.body
        stream = io.BytesIO(post_data)
        python_data = JSONParser().parse(stream)
        print(python_data['movie'])

        get_data = model_movies3.objects.get(id = id)
        print(get_data.movie)
        get_data.movie = python_data['movie']
        get_data.character = python_data['character']
        get_data.save()

        json_data = JSONRenderer().render(python_data)
        return HttpResponse(json_data, content_type = "application/json")

        # post_data = request.body
        # print(post_data)
        # # request_data = request.data.get("movie")
        # stream = io.BytesIO(post_data)
        # python_data = JSONParser().parse(stream)

        # print(python_data)        
         

        # id = model_movies3.objects.get(id = id)
        # object = {"id" : movie_data.id, "movie" : movie_data.movie, "character" : movie_data.character}
        # json_object = JSONRenderer().render(object)
        # return HttpResponse(json_object)


        # update_movie = model_movies3.data.get(id = id)
        # print(request.data.get('movie'))
        # update_movie.movie = request.data.get("movie")
        # print(update_movie.movie)
        # update_movie.character = request.data.get("character")

        # object = {"id" : update_movie.id, "movie" : update_movie.movie, "character" : update_movie.character}

        # update_movie.save()
        # return Response({"data" : object})
    
    if request.method == 'GET':

        print("get is rendering "+ str(id))
        
        ## single entry 
        movie_data = model_movies3.objects.get(id = id)
        # # return Response({'msg' : 'get is rendering.....'})
        # msg = {'msg' : 'get is rendering.....'}
        # json_data = JSONRenderer().render(msg['msg'])
        # # return HttpResponse(json_data, content_type = "appication/json")
        # object = {"id" : movie_data.id, "movie" : movie_data.movie, "character" : movie_data.character}
        # json_object = JSONRenderer().render(object)
        # return HttpResponse(json_object)

        ## with list
        movies_data = model_movies3.objects.all()
        print(movies_data[2].character)
        all_json = []
        for i in movies_data:
            print(i)
            object = {"id" : i.id, "movie" : i.movie, "character" : i.character}
            all_json.append(object)

        json_object = JSONRenderer().render(all_json)
        print(all_json)
        return HttpResponse(json_object, content_type = "application/json")

        ## with dictionary
        # movies_data = model_movies3.objects.all()
        # print(movies_data[2].character)
        # all_json = {}
        # for i in movies_data:
        #     print(i)
        #     object = {"id" : i.id, "movie" : i.movie, "character" : i.character}
        #     all_json[object['id']] = object

        # json_object = JSONRenderer().render(all_json)
        # print(all_json)
        # return HttpResponse(json_object, content_type = "application/json")


    if request.method == 'POST':
        all_data = model_movies3.objects.all()
        print("for all data + 1 means next entry: ", len(all_data) + 1)
        id = len(all_data) + 1
        print(request.body)
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        print(python_data)
        get_data_add = model_movies3.objects.create(movie = python_data['movie'], character = python_data['character'])
        get_data_add.save()

        # get_data = model_movies3.objects.filter(movie = python_data['movie'], character = python_data['character']).first()
        # object = {"id" : get_data.id, "movie" : get_data.movie, "character" : get_data.character}


        json_data = JSONRenderer().render(python_data)
        return HttpResponse(json_data, content_type = "application/json")

        # movie_instance = request.data.get('movie')
        # print(movie_instance)
        # get_data_add = model_movies3.objects.create(movie = request.data.get('movie'), character = request.data.get("character"))
        # get_data_add.save()

        # get_data_add.movie = request.data.get("movie")
        # print(get_data_add.movie)
        # get_data_add.character = request.data.get("character")
        # get_data_add.save()
        
        # return Response({"msg": "rendering ....."}, status = status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        print("rensering.....")
        get_data = model_movies3.objects.get(pk = id)
        # get_data = model_movies3.objects.filter(id = id).first()
        print(get_data)
        get_data.delete()
        
        msg = {"msg" : "is deleted"}
        json_data = JSONRenderer().render(msg['msg'])
        return HttpResponse(json_data, content_type = "application/json") 


# generic views without serializers
class movies_list_class1(ListAPIView):
    queryset = model_movies3.objects.all()
    print("rendering....!")
    serializer_class = movies3_serializers
    def get(self, request, *args, **kwargs):
        data = request.data


#     list_data = []
#     for i in queryset:
#         object = {"id" : i.id, "movie" : i.movie, "character" : i.character}
#         list_data.append(object)
#     # print(list_data)
#     bytes_data = JSONRenderer().render(list_data)
#     # stream = io.BytesIO(bytes_data)
#     # python_data = JSONParser().parse(stream)
#     serializer_class = movies3_serializers


    
    # serializer_class = bytes_data
    # print(serializer_class)

    # print(queryset)
    # stream = io.BytesIO(queryset)
    # python_data = JSONParser().parse(stream)
    # print(python_data)
    # serializer_class = movies3_serializers
    # print(serializer_class)

    # movies_data = model_movies3.objects.all()
    #     print(movies_data[1].character)
    #     all_json = []
    #     for i in movies_data:
    #         print(i)
    #         object = {"id" : i.id, "movie" : i.movie, "character" : i.character}
    #         all_json.append(object)

    #     json_object = JSONRenderer().render(all_json)
    #     print(all_json)
    #     return HttpResponse(json_object, content_type = "application/json")


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

        serializer = movies3_serializers(data=python_data)
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


# authentication and permissions

#  authentication :  basic authenticaton, premissions : isauthentication, allowany
class movie_auth_perm(viewsets.ModelViewSet):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class movies_list_class2(ListCreateAPIView):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

# authentication : session authentication, permissions : ISAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions, CustomPermissions
class movies_session_auth(viewsets.ModelViewSet):
    queryset = model_movies3.objects.all()
    serializer_class = movies3_serializers
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [DjangoObjectPermissions]
    permission_classes = [custom_get_permission]


# class movies_list_session_auth(ListAPIView):
#     queryset = model_movies3.objects.all()
#     serializer_class = movies3_serializers
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def decorators_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        # id = request.data.get('id')
        if id is not None:
            movie = model_movies3.objects.get(id = id)
            serializer = movies3_serializers(movie)
            return Response(serializer.data)
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        # post_data = request.body.get("id")
        serializer = movies3_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return(serializer.errors)

    if request.method == 'PUT':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_200_OK)
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)
        
    if request.method == 'PATCH':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies3.objects.get(id = id)
        serializer = movies3_serializers(movie, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'rendering.....', 'object': serializer.data}, status = status.HTTP_200_OK)
        movie = model_movies3.objects.all()
        serializer = movies3_serializers(movie, many = True)
        return Response(serializer.errors, status = status.HTTP_204_NO_CONTENT)

    if request.method == 'DELETE':
        id = pk
        # post_data = request.body.get("id")
        movie = model_movies3.objects.get(id = id)
        movie.delete()
        return Response({'msg':'rendering.....'}, status = status.HTTP_200_OK)









