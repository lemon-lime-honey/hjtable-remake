from django.contrib.auth import get_user_model
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipe"
    )
    content = models.TextField(max_length=1000, blank=True, null=True)
    category = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time = models.IntegerField()
    difficulty = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")


    def __str__(self):
        return self.title


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='step')
    detail = models.TextField()


    def __str__(self):
        return self.recipe.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipeingredient'
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True, null=True)


class RecipeReview(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='review'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='review'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)