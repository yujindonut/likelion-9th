from django import forms
from .models import *

class InfoForm(forms.ModelForm):
    class Meta:
        model = WriteInfoModel
        fields = ['webtoon_name', 'genre', 'text', 'image']

#댓글
class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000, 
        widget=forms.Textarea(attrs={'rows':'3', 'cols': '50'}))
    class Meta:
        model = Comment
        fields =['body']