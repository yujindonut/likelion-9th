from django import forms
from .models import WebtoonModel

class WebtoonForm(forms.ModelForm):
    class Meta:
        model = WebtoonModel
        fields = ['webtoon_name', 'genre', 'writer', 'text', 'image']