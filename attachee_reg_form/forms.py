from pyexpat import model
from unicodedata import name
from django import forms
from .models import Form


class UpdateForm(forms.ModelForm):
    class Meta:
        model= Form
        fields ='__all__'