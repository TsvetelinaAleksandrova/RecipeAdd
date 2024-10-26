from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from RecipesApp.profiles.models import Profile
from RecipesApp.recipes.choices import CuisineTypeChoices


class Recipe(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(10),
        ],
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': "We already have a recipe with the same title!",
        },
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices.choices,
        null=False,
        blank=False,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Ingredients must be separated by a comma and space.",
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        null=False,
        blank=False,
        help_text="Provide the cooking time in minutes.",
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name="recipes"
    )

