# Generated by Django 4.2.13 on 2024-08-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_news_recipe_ingredients_recipe_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(),
        ),
    ]
