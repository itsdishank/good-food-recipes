# Generated by Django 3.1.3 on 2020-12-02 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_remove_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeimage',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='recipe.recipe'),
        ),
    ]
