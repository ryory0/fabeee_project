from rest_framework import routers
from .views import RecipeViewSet, CommentViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'recipe', RecipeViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'product', ProductViewSet)