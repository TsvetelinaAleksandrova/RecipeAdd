from django import forms

from RecipesApp.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['bio']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Profile
        fields = ()