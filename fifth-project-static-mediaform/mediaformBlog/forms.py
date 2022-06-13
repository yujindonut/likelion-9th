from django import forms
from .models import mediaformBlog

#장고에서 지원해주는 forms를 받는다
class BlogForm(forms.ModelForm):
    class Meta: #이름표와 같은 역할 : Blog모델에 이러한 fileds를 연결시키는 역할 제공
        model = mediaformBlog
        fields = ['subject', 'drafter', 'textBody', 'picture']
        #date는 작성된 시간을 자동으로 넣어주는 기능이여서 입력을 받는 것이 아님
        #form을 띄어줄때 title, drafter, textBody, picture 넣어줌


