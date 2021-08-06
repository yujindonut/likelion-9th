from django import forms
from .models import *

# Create your models here.
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields =['title','hideName','body','image']

 
CATEGORY_CHOICES =(
    ("0", "10세 미만"),
    ("1", "10대"),
    ("2", "20대"),
    ("3", "30-40대"),
    ("4", "50-60대"),
    ("5", "70세 이상"),
    ("6", "모더나"),
    ("7", "화이자"),
    ("8", "아스트라제네카"),
    ("9", "얀센"),
    ("10", "자유게시판"),
)
class CategoryForm(forms.Form):
    category_field = forms.MultipleChoiceField(choices = CATEGORY_CHOICES)

#댓글
class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000, 
        widget=forms.Textarea(attrs={'rows':'3', 'cols': '50'}))
    class Meta:
        model = Comment
        fields =['body','hideName']


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')