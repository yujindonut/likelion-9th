from django import forms
from .models import Blog

# Create your models here.
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields =['title','body','image']