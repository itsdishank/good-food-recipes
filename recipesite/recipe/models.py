from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from slugify import slugify
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
	STATUS_CHOICES = (('draft','Draft'),('published','Published'))
	title = models.CharField(max_length=256)
	description = models.TextField(null=True)
	slug = models.SlugField(max_length=264,unique_for_date='publish')
	user = models.ForeignKey(User,related_name='recipe_post',on_delete=models.CASCADE)
	ingredients = models.TextField(null=True)
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	prep_time = models.IntegerField()
	cook_time = models.IntegerField()
	servings = models.IntegerField()
	yields = models.CharField(max_length=256)
	tags=TaggableManager()

	def first_image(self):
		return self.images.first()


	class Meta:
		ordering=('-publish',)

	def __str__(self):
		return self.title 

	def get_absolute_url(self):
		return reverse('recipe_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class RecipeImage(models.Model):
    recipe = models.ForeignKey(Recipe, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.recipe.title	
