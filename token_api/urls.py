from django.urls import path, include
from . import views
from token_api.views import *
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

# creating router object
router = DefaultRouter()

router.register("movies_auth", views.movies_auth, basename="movies_auth"),
router.register("movies_auth1", views.movies_auth1, basename="movies_auth1"),

urlpatterns = [
    # path("admin/", admin.sites.urls),
    path("decorators_movies_api/", views.decorators_movies_api),
    path("decorators_movies_api/<int:pk>", views.decorators_movies_api),
    path("movie_generic_api/", movie_generic_api.as_view()),
    path("get_token/", obtain_auth_token),
    path("gettoken/", TokenObtainPairView.as_view(), name='taken_obtain_pair'),
    path("refreshtoken/", TokenRefreshView.as_view(), name='token_refresh'),
    path("verifytoken/", TokenVerifyView.as_view(), name='verifytoken'),
    path("", include(router.urls)),
    # path("movies_auth/", views.movies_auth, name="movies_auth"),
    path("jwt_create/", views.jwt_create, name="jwt_create"),
    path("jwt_get/", views.jwt_get, name="jwt_get"),
    path("jwt_put/", views.jwt_put, name="jwt_put"),
    path("jwt_poc/", views.jwt_poc, name="jwt_poc"),
    path("get_all_data/", views.get_all_data, name="get_all_data"),
    path("create_user_kyc/", views.create_user_kyc, name="create_user_kyc"),
    path("get_user_kyc/", views.get_user_kyc, name="get_user_kyc"),
    path("update_user_kyc/", views.update_user_kyc, name="update_user_kyc"),
    path("get_user_kyc_info/", views.get_user_kyc_info, name="get_user_kyc_info"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)