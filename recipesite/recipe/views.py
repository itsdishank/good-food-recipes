from django.shortcuts import render ,get_object_or_404,redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
# from recipe.forms import RecipeForm,ImageForm,CreateUserForm
from recipe.forms import CreateUserForm
from recipe.models import RecipeImage,Recipe
from taggit.models import Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
            

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def recipe_home_page_view(request):
    recipe_list=Recipe.objects.all()
    return render(request,'recipe/homepage.html')

def about_view(request):
    return render(request,'recipe/About.html')

@login_required(login_url='login')
def profile_view(request):
    logged_in_user = request.user
    logged_in_user_posts = Recipe.objects.filter(user=logged_in_user)

    # return render(request, 'index.html', {'posts': logged_in_user_posts})
    return render(request,'recipe/profile_page.html', {'recipe_list': logged_in_user_posts})

def recipe_list_view(request,tag_slug=None):
    recipe_list=Recipe.objects.filter(status='published')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        recipe_list=Recipe.objects.filter(status='published',tags__in=[tag])

    paginator=Paginator(recipe_list,3)
    page_number=request.GET.get('page')
    try:
        recipe_list=paginator.page(page_number)
    except PageNotAnInteger:
        recipe_list=paginator.page(1)
    except EmptyPage:
        recipe_list=paginator.page(paginator.num_pages)
    return render(request,'recipe/recipes_list.html',{'recipe_list':recipe_list,'tag':tag })
    
def recipe_detail_view(request,year,month,day,recipe):
    recipe = get_object_or_404(Recipe,slug=recipe,status='published',publish__year=year,publish__month=month,publish__day=day)
    photos = RecipeImage.objects.filter(recipe=recipe)
    split_ingredients = recipe.ingredients.split("\n")
    split_body = recipe.body.split("\n")
    total_time = recipe.prep_time + recipe.cook_time
    
    # comments=recipe.comments.filter(active=True)
    # csubmit=False
    # if request.method=='POST':
    #     form=CommentForm(request.POST)
    #     if form.is_valid():
    #         new_comment=form.save(commit=False)
    #         new_comment.recipe=recipe
    #         new_comment.save()
    #         csubmit=True
    # else:
    #     form=CommentForm()
    return render(request,'recipe/recipe_details.html',{'recipe':recipe,'split_ingredients':split_ingredients,'split_body':split_body,'total_time':total_time,'photos':photos})

@login_required(login_url='login')
def upload_recipe_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        # tags = request.POST.get('tags')
        # tags = request.POST.get('tags').split(",")
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        body = request.POST.get('body')
        status = request.POST.get('status')
        prep_time = request.POST.get('prep_time')
        cook_time = request.POST.get('cook_time')
        servings = request.POST.get('servings')
        yields = request.POST.get('yields')
        slug = request.POST.get('title').replace(' ', '-').lower()
        user = request.user

        recipe = Recipe.objects.create(
            title=title,
            description=description,
            # tags=tags,
            ingredients=ingredients,
            body=body,
            status=status,
            prep_time=prep_time,
            cook_time=cook_time,
            servings=servings,
            yields=yields,
            slug=slug,
            user=user
        )
        
        for file_num in range(0, int(length)):
            RecipeImage.objects.create(
                recipe=recipe,
                images=request.FILES.get(f'images{file_num}')
            )


    return render(request,'recipe/upload_recipe.html')
