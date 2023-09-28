from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


    def create(self, request, *args, **kwargs):
        if request.data.get('ingredients'):
            for i in range(len(request.data['ingredients'])):
                ingredient = request.data['ingredients'][i]['ingredient']
                if isinstance(ingredient, str):
                    try:
                        ig = Ingredient.objects.get(name=ingredient).pk
                    except:
                        ig = Ingredient.objects.create(name=ingredient).pk
                    request.data['ingredients'][i]['ingredient'] = ig
        return super().create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        if request.data.get('ingredients'):
            for i in range(len(request.data['ingredients'])):
                ingredient = request.data['ingredients'][i]['ingredient']
                if isinstance(ingredient, str):
                    try:
                        ig = Ingredient.objects.get(name=ingredient).pk
                    except:
                        ig = Ingredient.objects.create(name=ingredient).pk
                    request.data['ingredients'][i]['ingredient'] = ig
        return super().update(request, *args, **kwargs)