from django.db import models


# Create your models here.
class Blog(models.Model):
    #이 Model이라는 클래스 안에 id값이 이미 정의되어있다! --> 따로 id콜럼을 안만들어줘도 됨
    subject = models.CharField(max_length = 200) #title
    drafter = models.CharField(max_length = 100) #writer #제한이 있는 문자열
    date = models.DateTimeField() #pub_date
    textBody = models.TextField() #body #제한이 없는 문자열

    #blog object라고 보이지 않고, 우리가 지정한 title이름이 보이게 하는
    def __str__(self): #객체가 호출이 될때 글의 제목이 볼 수 있게끔한다.
        return self.name #/admin/의 페이지에서 제목으로 이름이 보인다.

    def summary(self):
        return self.textBody[:100] #100번째 index까지 문자열을 잘라줌

