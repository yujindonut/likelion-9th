from django import forms
from .models import Message
#from .models import Reply
# Create your models here.
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields =['to','body']

class MessageToMeForm(forms.ModelForm):
    class Meta:
        model = Message
        fields =['body']       
'''
class ReplyForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000, 
        widget=forms.Textarea(attrs={'rows':'3', 'cols': '50'}))
    class Meta:
        model = Reply
        fields =['to','body']
'''

