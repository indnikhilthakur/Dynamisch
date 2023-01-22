from django.urls import path
from practice_api import views


urlpatterns = [
    path("all_movies/", views.all_movies, name="all_movies"),
    path("movie_data/<int:id>", views.movie_data, name="movie_data"),
    path("movie_d/", views.movie_d, name="movie_d"),
    path("get_movie_d/<int:id>", views.get_movie_d, name="get_movie_d"),
    path("create_movie/", views.create_movie, name="create_movie"),
    path("get_data/", views.get_data, name="get_data"),
    path("get_data/<int:id>", views.get_data, name="get_data"),
    path("movie_api/", views.movie_api.as_view(), name="movie_api"),
    # path("movie_list/", movie_list.as_view(), name= "movie_list"),
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

]