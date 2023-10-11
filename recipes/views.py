from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


    def new_ingredient(self, request):
        if request.data.get('ingredients'):
            for i in range(len(request.data['ingredients'])):
                ingredient = request.data['ingredients'][i]['ingredient']
                if isinstance(ingredient, str):
                    try:
                        ig = Ingredient.objects.get(name=ingredient).pk
                    except:
                        ig = Ingredient.objects.create(name=ingredient).pk
                    request.data['ingredients'][i]['ingredient'] = ig

        return request


    def create(self, request, *args, **kwargs):
        request = self.new_ingredient(request)
        return super().create(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        request = self.new_ingredient(request)
        return super().update(request, *args, **kwargs)


class RecipeReviewViewSet(ModelViewSet):
    serializer_class = RecipeReviewSerializer
    queryset = RecipeReview.objects.all()


    def get_queryset(self):
        recipe = get_object_or_404(Recipe, pk=self.kwargs.get('recipe_pk'))
        return super().get_queryset().filter(recipe=recipe)