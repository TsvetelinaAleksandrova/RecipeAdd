from django.shortcuts import render

from RecipesApp.profiles.models import Profile


def home_page(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, template_name='common/home-page.html', context=context)