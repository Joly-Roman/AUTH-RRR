from django import forms
from .models import *


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age']