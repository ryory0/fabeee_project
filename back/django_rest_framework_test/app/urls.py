from rest_framework import routers
from .views import RecipeViewSet

router = routers.DefaultRouter()
router.register(r'recipe', RecipeViewSet)