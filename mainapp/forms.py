from django import forms
from django.forms import ModelForm
from mainapp.models import Tankcalcmetric

class TankcalcmetricForm(forms.ModelForm):
    class Meta:
        model= Tankcalcmetric
        fields= '__all__'
        exclude = ('calcid',)
        