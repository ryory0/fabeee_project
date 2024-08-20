from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Recipe, Comment, Product
from .serializers import RecipeSerializer, CommentSerializer, ProductSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        comment = self.get_object()
        comments = comment.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def recipes(self, request, pk=None):
        product = self.get_object()
        recipes = product.recipes.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)