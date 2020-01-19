from .models import Neighbourhood,Profile
from django import forms

class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin','post']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']
