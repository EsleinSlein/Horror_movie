from django.forms import forms, ModelForm
from .models import Movies


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

