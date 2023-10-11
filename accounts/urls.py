from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('password/', ChangePasswordView.as_view(), name='change_password'),
    path('update/', UserUpdateView.as_view(), name='user_update'),
    path('delete/', UserDeleteView.as_view(), name='user_delete'),
]