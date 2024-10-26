from django.core.exceptions import ValidationError


def validate_nickname_length(value):
    if len(value) < 2:
        raise ValidationError("Nickname must be at least 2 chars long!")


def validate_capital_letter(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")