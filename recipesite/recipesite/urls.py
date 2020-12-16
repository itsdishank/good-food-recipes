"""recipesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipe_home_page_view, name="home"),
    path('upload_recipe/', views.upload_recipe_view, name='upload_recipe'),
    path('recipe_list/', views.recipe_list_view, name='blog'),
    re_path('tag/(?P<tag_slug>[-\w]+)/', views.recipe_list_view, name='recipe_list_by_tag_name'),
    path('about/', views.about_view),
    path('profile/', views.profile_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    re_path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<recipe>[-\w]+)/', views.recipe_detail_view,name='recipe_detail'),
    # re_path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<recipe>[-\w]+)/', views.recipe_detail_view, name='recipe_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

