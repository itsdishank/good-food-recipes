# from django.contrib import admin
# from recipe.models import Recipe,Image

# # Register your models here.

# class RecipeAdmin(admin.ModelAdmin):
	# list_display=['title','slug','user','body','publish','created','updated','status','prep_time','cook_time','yields']
	# list_filter=('status','user','created','publish')
	# search_fields=('title','ingredients','body')
	# raw_id_fields=('user',)
	# date_hierarchy='publish'
	# ordering=['status','publish']
	# prepopulated_fields={'slug':('title',)}

# class ImageAdmin(admin.ModelAdmin):
# 	list_display=['image']
# 	raw_id_fields=('recipe',)



# admin.site.register(Recipe,RecipeAdmin)
# admin.site.register(Image,ImageAdmin)

from django.contrib import admin

from .models import Recipe, RecipeImage

class RecipeImageAdmin(admin.StackedInline):
    model = RecipeImage

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
	inlines = [RecipeImageAdmin]
	list_display=['title','slug','user','body','publish','created','updated','status','prep_time','cook_time','yields']
	list_filter=('status','user','created','publish')
	search_fields=('title','ingredients','body')
	raw_id_fields=('user',)
	date_hierarchy='publish'
	ordering=['status','publish']
	prepopulated_fields={'slug':('title',)}

	class Meta:
		model = Recipe

@admin.register(RecipeImage)
class RecipeImageAdmin(admin.ModelAdmin):
    pass