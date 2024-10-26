from django.urls import path, include

from RecipesApp.recipes import views

urlpatterns = (
    path('create/', views.create_recipe_page, name='create-recipe'),
    path('catalogue/', views.catalogue_page, name='catalogue'),
    path('<int:recipe_id>/', include([
        path('details/', views.recipe_details_page, name='details-recipe'),
        path('edit/', views.edit_recipe_page, name='edit-recipe'),
        path('delete/', views.delete_recipe_page, name='delete-recipe'),
    ]))
)

