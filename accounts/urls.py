from django.urls import path, include
from .views import *

urlpatterns = [
    path('', SignupAPIView.as_view()),
    path('', include('rest_framework.urls'))
]