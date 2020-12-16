from django import forms
# from recipe.models import Recipe, Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ('title','description','ingredients','body','status','prep_time','cook_time','servings','yields')
#      #    labels = {
#      #    	'body': ('Writer'),
#     	# }

 
# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image')    
#     class Meta:
#         model = Image
#         fields = ('image', )
#      #    labels = {
#      #    	"image": "Enter images"
#     	# }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
