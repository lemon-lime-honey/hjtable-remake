from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]