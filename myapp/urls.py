from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
]