from django.db import models

# Create your models here.

#클래스의 이름은 테이블과 같아야함
#models이라는 클래스를 상속받음
class Blog(models.Model) : 
    #Model 안에 이미 id가 정의되어있다!
    #제한이 있는 문자열 .CharField
    name = models.CharField(max_length = 200) #title
    drafter = models.CharField(max_length = 100) #writer
    date = models.DateTimeField() #pub_date
    textBody = models.TextField() #body / 제한이 없는 field

#Django의 데이터베이스는 아무나 들어가서 변경할 수 없음
#python manage.py createsuperuser를 사용해서 데이터베이스에 권한을 만들어야한다

    def __str__(self): #객체가 호출이 될때 글의 제목이 볼 수 있게끔한다.
        return self.name #/admin/의 페이지에서 제목으로 이름이 보인다.

    def summary(self):
        return self.textBody[:100] #100번째 index까지 문자열을 잘라줌