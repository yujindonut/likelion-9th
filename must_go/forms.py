from django import forms
from .models import MustGo

class FoodBlogForm(forms.ModelForm):
    class Meta:
        model = MustGo
        fields = ['restaurant', 'rate', 'text', 'image']
        #date는 작성된 시간을 자동으로 넣어주는 기능이여서 입력을 받는 것이 아님