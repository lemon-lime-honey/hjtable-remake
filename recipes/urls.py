from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'', RecipeViewSet)
router.register(r'(?P<recipe_pk>\d+)/reviews', RecipeReviewViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
