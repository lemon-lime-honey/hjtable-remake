from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()