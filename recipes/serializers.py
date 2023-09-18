from rest_framework.serializers import ModelSerializer
from .models import *


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeIngredientSerializer(ModelSerializer):
    ingredient = IngredientSerializer(source='recipeingredient_set')


    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'quantity',)


class RecipeStepSerializer(ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ('detail',)


class RecipeSerializer(ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True)
    steps = RecipeStepSerializer(many=True, source='step')


    class Meta:
        model = Recipe
        fields = (
            'title',
            'content',
            'category',
            'time',
            'difficulty',
            'ingredients',
            'steps'
        )