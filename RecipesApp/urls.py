
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RecipesApp.common.urls')),
    path('recipe/', include('RecipesApp.recipes.urls')),
    path('profile/', include('RecipesApp.profiles.urls')),
]
