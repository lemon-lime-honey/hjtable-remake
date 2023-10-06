from rest_framework.serializers import ModelSerializer
from .models import *


class RecipeIngredientSerializer(ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'quantity',)


class RecipeStepSerializer(ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ('detail',)


class RecipeSerializer(ModelSerializer):
    ingredients = RecipeIngredientSerializer(many=True, source='recipeingredient')
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


    def create(self, validated_data):
        steps = validated_data.pop('step')
        ingredients = validated_data.pop('recipeingredient')
        recipe = Recipe.objects.create(
            **validated_data,
            user=self.context.get('request').user
        )

        for step in steps:
            RecipeStep.objects.create(recipe=recipe, detail=step['detail'])

        for ingredient in ingredients:
            RecipeIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient['ingredient'],
                quantity=ingredient['quantity']
            )

        return recipe


    def update(self, instance, validated_data):
        if self.partial:
            if 'step' in self.initial_data:
                validated_data['step'] = self.initial_data['step']
            if 'recipeingredient' in self.initial_data:
                validated_data['recipeingredient'] = self.initial_data['recipeingredient']

        if 'step' in validated_data:
            steps = validated_data.pop('step')
            original_steps = RecipeStep.objects.filter(recipe=instance)

            index = 0

            for st in original_steps:
                if index < len(steps):
                    st.detail = steps[index]['detail']
                    st.save()
                else:
                    st.delete()
                index += 1

            if index < len(steps):
                for i in range(index, len(steps)):
                    RecipeStep.objects.create(
                        recipe=instance,
                        detail=steps[i]['detail']
                    )

        if 'recipeingredient' in validated_data:
            ingredients = validated_data.pop('recipeingredient')
            original_ingredients = RecipeIngredient.objects.filter(recipe=instance)
            index = 0

            for ri in original_ingredients:
                if index < len(ingredients):
                    ri.ingredient = ingredients[index]['ingredient']
                    ri.quantity = ingredients[index]['quantity']
                    ri.save()
                else:
                    ri.delete()
                index += 1

            if index < len(ingredients):
                for i in range(index, len(ingredients)):
                    RecipeIngredient.objects.create(
                        recipe=instance,
                        ingredient=ingredients[i]['ingredient'],
                        quantity=ingredients[i]['quantity']
                    )

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.time = validated_data.get('time', instance.time)
        instance.difficulty = validated_data.get('difficulty', instance.difficulty)
        instance.save()

        return instance


class RecipeReviewSerializer(ModelSerializer):
    class Meta:
        model = RecipeReview
        fields = ('content',)


    def create(self, validated_data):
        recipe = Recipe.objects.get(
            pk=self.context.get('request').path.split('/')[2]
        )
        user = self.context.get('request').user
        review = RecipeReview.objects.create(
            recipe=recipe,
            user=user,
            content=validated_data.get('content')
        )

        return review