from django.db import models

class mediaformBlog(models.Model):
    subject = models.CharField(max_length = 200) 
    drafter = models.CharField(max_length = 100) 
    date = models.DateTimeField() 
    textBody = models.TextField() 
    picture = models.ImageField(upload_to = "mediaformBlog/", blank = True, null = True) #image #사진을 안올릴 수도 있어서, blank와 nul을 모두 true처리
    #upload_to는 업로드할 폴더를 지정하는 것 
    #settings.py에 MEDIA_URL로 지정해둔 media폴더 안에 mediaformBlog폴더를 만들어서 관리
    #blog/~이런식으로 url경로가 적힘 / 실제 사진이 저장되는 것이 아니라 사진이 있는 경로가 저장되는 것임
    #데이터가 추가 되거나 모델에 변경이 생기면, 기존에 있던 데이터들을 삭제해줘야한다..

    #blog object라고 보이지 않고, 우리가 지정한 title이름이 보이게 하는
    def __str__(self): #객체가 호출이 될때 글의 제목이 볼 수 있게끔한다.
        return self.name #/admin/의 페이지에서 제목으로 이름이 보인다.

    def summary(self):
        return self.textBody[:100] #100번째 index까지 문자열을 잘라줌

