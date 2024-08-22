from django.contrib import admin

from django.contrib import admin
from .models import Product, Recipe, Comment, News

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)
    list_filter = ('price',)
    filter_horizontal = ('recipes',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'created_at')
    search_fields = ('context',)
    list_filter = ('created_at',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
