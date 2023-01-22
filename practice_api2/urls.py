from django.urls import path
from practice_api2 import views

urlpatterns = [
    path("get-movies2", views.get_movies2, name="get_movies2"),
    

]