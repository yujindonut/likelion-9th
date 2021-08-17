from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class WebtoonModel(models.Model):
    webtoon_name = models.CharField(max_length=100) #웹툰 이름
    genre_Choices = (
    ('일상','일상'),
    ('개그','개그'),
    ('판타지','판타지'),
    ('액션','액션'),
    ('드라마/순정/감성','드라마/순정/감성'),
    ('시대극','시대극'),
    ('호러/스릴러','호러/스릴러'),
    )
    genre = models.TextField(choices=genre_Choices) #장르
    writer = models.CharField(max_length = 100) #작성자
    text = models.TextField() #웹툰 정보
    date = models.DateTimeField() #날짜
    image = models.ImageField(upload_to = "webtoonpage/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200,200)],
                                           options={'quality': 100})

    def __str__(self):
        return self.name 

    def summary(self):
        return self.textBody[:50] 

class Comment(models.Model):
    post_id = models.ForeignKey("WebtoonModel",on_delete=models.CASCADE,db_column="post_id")
    comment_id = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    writer = models.CharField(max_length=10)
    body = models.TextField('댓글')
    pub_date=models.DateTimeField()
       

