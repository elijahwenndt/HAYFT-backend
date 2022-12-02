from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
