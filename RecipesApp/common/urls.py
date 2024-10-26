from django.urls import path

from RecipesApp.common import views

urlpatterns = (
    path('', views.home_page, name='home'),
)