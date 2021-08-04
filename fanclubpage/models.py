from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class unnie_info(models.Model):
    foodInfo = models.CharField(max_length=100) #여수언니 먹방 정보
    subject = models.CharField(max_length = 100) #장르
    text = models.TextField() #팬들의 여수언니 칭찬, 잡담
    date = models.DateTimeField() #날짜
    image = models.ImageField(upload_to = "fanclub/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200,200)],
                                           options={'quality': 100})

    def __str__(self): #객체가 호출이 될때 글의 제목이 볼 수 있게끔한다.
        return self.name #/admin/의 페이지에서 제목으로 이름이 보인다.

    def summary(self):
        return self.textBody[:100] #100번째 index까지 문자열을 잘라줌