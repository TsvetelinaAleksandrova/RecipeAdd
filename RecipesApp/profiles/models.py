from django.core.validators import MinLengthValidator
from django.db import models

from RecipesApp.profiles.validators import validate_capital_letter, validate_nickname_length


class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[
            validate_nickname_length,
        ],
        null=False,
        blank=False,
        unique=True,
    )

    first_name = models.CharField(
        max_length=30,
        validators=[
            validate_capital_letter,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            validate_capital_letter,
        ],
        null=False,
        blank=False,
    )

    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )