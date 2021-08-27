from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class WriteInfoModel(models.Model):
    title = models.CharField(max_length=100) #글 작성 제목
    location_Choices = (
    ('서울','서울'),
    ('인천/경기','인천/경기'),
    ('강원','강원'),
    ('대전/충청','대전/충청'),
    ('광주/전라','광주/전라'),
    ('부산/대구/경상','부산/대구/경상'),
    ('제주','제주'),
    )
    location = models.TextField(choices=location_Choices) #위치
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #작성자
    text = models.TextField() #빵투어 정보
    date = models.DateTimeField() #날짜
    # latitude = models.TextField() #위도
    # longitude = models.TextField() #경도
    image = models.ImageField(upload_to = "tripinfo/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200,200)],
                                           options={'quality': 100})
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like", blank=True)
    post_hit = models.PositiveIntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.title 

    def summary(self):
        return self.textBody[:50] 

    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()
        

class Meta:
    ordering = ['-created']
    
class Comment(models.Model):
    post_id = models.ForeignKey("WriteInfoModel",on_delete=models.CASCADE,db_column="post_id")
    comment_id = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField('댓글')
    pub_date=models.DateTimeField()
       
    def summary(self):
        return self.body[:10]    

