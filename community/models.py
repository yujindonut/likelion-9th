from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    writer=models.CharField(max_length=100)
    hideName = models.BooleanField()
    pub_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=True,null=True)
    CustomUser = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80] 


class Comment(models.Model):
    postId = models.ForeignKey("Blog",on_delete=models.CASCADE,db_column="blogId")
    comment_id = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    hideName = models.BooleanField()
    writer = models.CharField(max_length=50)
    body = models.TextField('댓글')
    pub_date=models.DateTimeField()
    CustomUser = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, null=False)