from django.urls import path, include

from RecipesApp.profiles import views

urlpatterns = (
    path('create/', views.create_profile_page, name='create-profile'),
    path('details/', views.profile_details_page, name='details-profile'),
    path('edit/', views.edit_profile_page, name='edit-profile'),
    path('delete/', views.delete_profile_page, name='delete-profile'),
)
