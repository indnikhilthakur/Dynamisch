"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from practice_api import views
# from practice_api.views import *

# from practice_api2 import views

from practice_api3.views import *
from practice_api3 import views
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

# register student viewset with router
router.register("movie_viewset_class", views.movie_viewset_class, basename="movie_viewset_class"),
router.register("movie_model_viewset", views.movie_model_viewset, basename="movie_model_viewset"), 
router.register("movie_readonlymodelviewset", views.movie_readonlymodelviewset, basename="movie_readonlymodelviewset"),
router.register("movie_auth_perm", views.movie_auth_perm, basename = "movie_auth_perm"),
# router.register("movies_list_session_auth", views.movies_list_session_auth),
router.register("movies_session_auth", views.movies_session_auth, basename = "session_auth"),


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("all_movies/", views.all_movies, name="all_movies"),
    # path("movie_data/<int:id>", views.movie_data, name="movie_data"),
    # path("movie_d/", views.movie_d, name="movie_d"),
    # path("get_movie_d/<int:id>", views.get_movie_d, name="get_movie_d"),
    # path("create_movie/", views.create_movie, name="create_movie"),
    # path("get_data/", views.get_data, name="get_data"),
    # path("get_data/<int:id>", views.get_data, name="get_data"),
    # path("post_data/", views.post_data, name = "post_data"),
    # path("put_data/", views.put_data, name="put_data"),
    # path("api_msg/", views.api_msg, name="api_msg"),
    # path("post_msg/", views.post_msg, name="post_msg"),
    # path("get_post_msg/", views.get_post_msg, name="get_post_msg"),
    # path("movie_list/", movie_list.as_view(), name= "movie_list"),
    # # path("crud/", views.crud),
    # path("crud/<int:id>", views.crud),
    # path("get_all_data/", views.get_all_data, name="get_all_data"),
    # path("movie_api/", views.movie_api.as_view(), name="movie_api"),
    # path("movies_list_class/", movies_list_class.as_view(), name="movies_list_class "),
    # path("movie_create_class/", movie_create_class.as_view(), name="movie_create_class "),
    # path("movie_update_class/<int:pk>", movie_update_class.as_view(), name="movie_update_class "),
    # path("movie_retrieve_class/<int:pk>", movie_retrieve_class.as_view(), name="movie_retrieve_class "),
    # path("movie_destroy_class/<int:pk>", movie_destroy_class.as_view(), name="movie_destroy_class "),
    # path("movie_list_create_class/", movie_list_create_class.as_view(), name="movie_list_create_class "),
    # path("movie_retrieve_update_class/<int:pk>", movie_retrieve_update_class.as_view(), name="movie_retrieve_update_class "),
    # path("movie_retrieve_destroy_class/", movie_retrieve_destroy_class.as_view(), name="movie_update_class "),
    # path("movie_retrieve_update_destroy_class/", movie_retrieve_update_destroy_class.as_view()),
    # path("movie_retrieve_update_destroy_class/<int:pk>", movie_retrieve_update_destroy_class.as_view()),
    # # get views as single url
    # path("concreate_views", concreate_generic_views_class_list_create.as_view()),
    # path("concreate_views/<int:pk>", concreate_generic_views_class_retrieve_update_destroy.as_view()),
    # path("", include("practice_api2.urls")),
    # path("", include("practice_api.urls")),


    # path('users/', movie_list.as_view(queryset=model_movie.objects.all(), serializer_class=movies_serializers), name='user-list'),
    # path("movie_list_list", views.movie_list.list , name= "movie_list_list"),
    # path("movie_d/<int:id>", views),
    # path("", include("practice_api.urls")),

    # practice_api2
    # path("get_movies2/", views.get_movies2, name="get_movies2"),
    # path("create_movies2/", views.create_movie2, name="create_movies2"),
    # path("put_movies2/<int:pk>", views.put_movies2),
    # path("put_movies2/", views.put_movies2),

    # pracctice_api3
    path("get_data_movies/", views.get_data_movies, name = "get_data_movies"),
    # path("get_data_movie_id/", views.get_data_movie_id),
    path("get_data_movie_id/<int:pk>", views.get_data_movie_id),
    # path("get_data_movie/", views.get_data_movie, name = "get_data_movie"),
    path("get_all_views/", views.get_all_views, name = "get_all_views"),
    path("get_id_view/<int:pk>", views.get_id_view, name = "get_id_view"),
    path("movies_list_class/", movies_list_class.as_view()),
    path("movie_retrieve_class/<int:pk>", movie_retrieve_class.as_view()),
    path("concreate_generic_views_class_retrieve_update_destroy/<int:pk>", concreate_generic_views_class_retrieve_update_destroy.as_view()),

    # create api
    path("create_api/", views.create_api),
    path("create_api_post/", views.create_api_post),
    path("create_api_class/", create_api_class.as_view()),
    path("create_list_class/", create_list_class.as_view()),
    path("create_api_generic_lc/", create_api_generic_lc.as_view()),


    # api view crud
    path("api_view_class/", api_view_class.as_view()),
    path("get_data_crud/", views.get_data_crud, name = "get_data_crud"),
    # path("get_data_crud/<int:pk>", views.get_data_crud)
    path("get_api_view_def/<int:pk>", views.get_api_view_def),
    path("get_api_view_def/", views.get_api_view_def),
    path("json_crud/", views.json_crud, name="json_crud"),
    path("movie_data/<int:id>", views.movie_data, name = "movie_data"),
    path("without_serializer/<int:id>", views.without_serializer, name = "without_serializer"),
    # path("movies_list_class1/", movies_list_class1.as_view()),
    path("generic_mixin_movie_data_list_create/", generic_mixin_movie_data_list_create.as_view()),
    path("generic_mixin_movie_retrieve_update_delete/<int:pk>", generic_mixin_movie_retrieve_update_delete.as_view()),
    path("", include(router.urls)),
    path("movies_list_class2/", movies_list_class2.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("decorators_api/", views.decorators_api),
    path("decorators_api/<int:pk>", views.decorators_api),
    path("", include('token_api.urls')),
    path("", include('rest_poc.urls'))






]
