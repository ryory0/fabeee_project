from rest_framework import serializers
from .models import Recipe, Comment, Product


class CommentSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), source='recipe.id')

    class Meta:
        model = Comment
        fields = ['created_at', 'context', 'recipe']

class RecipeSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'image', 'description', 'comments']

class ProductSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image', 'recipes']

