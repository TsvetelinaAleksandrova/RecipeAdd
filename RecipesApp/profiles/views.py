from django.shortcuts import render, redirect

from RecipesApp.profiles.forms import ProfileForm, EditProfileForm, DeleteProfileForm
from RecipesApp.recipes.models import Recipe
from RecipesApp.utils import get_profile


def create_profile_page(request):
    form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, template_name='profile/create-profile.html', context=context)


def profile_details_page(request):
    profile = get_profile()
    total_recipes = Recipe.objects.filter(author=profile).count()

    context = {
        'profile': profile,
        'total_recipes': total_recipes
    }

    return render(request, template_name='profile/details-profile.html', context=context)


def edit_profile_page(request):
    profile = get_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile_page(request):
    profile = get_profile()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/delete-profile.html', context)
