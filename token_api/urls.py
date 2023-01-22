from django.urls import path, include
from . import views
from token_api.views import *
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

router.register("movies_auth", views.movies_auth, basename="movies_auth"),
router.register("movies_auth1", views.movies_auth1, basename="movies_auth1"),

urlpatterns = [
    # path("admin/", admin.sites.urls),
    path("decorators_movies_api", views.decorators_movies_api),
    path("decorators_movies_api/<int:pk>", views.decorators_movies_api),
    path("movie_generic_api/", movie_generic_api.as_view()),
    path("get_token/", obtain_auth_token),
    path("gettoken/", TokenObtainPairView.as_view(), name='taken_obtain_pair'),
    path("refreshtoken/", TokenRefreshView.as_view(), name='token_refresh'),
    path("verifytoken/", TokenVerifyView.as_view(), name='verifytoken'),
    path("", include(router.urls)),
    # path("movies_auth/", views.                            movies_auth, name="movies_auth")
]