from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    writer=models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, null=False)
    hideName = models.BooleanField()
    pub_date=models.DateTimeField()
    body=models.TextField()
    image = models.ImageField(upload_to="mediaForm/",blank=True,null=True)
    
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:15] 


class Comment(models.Model):
    postId = models.ForeignKey("Blog",on_delete=models.CASCADE,db_column="postId")
    post_id = models.CharField(max_length=50)
    comment_id = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    hideName = models.BooleanField()
    writer = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, null=False)
    body = models.TextField('댓글')
    pub_date=models.DateTimeField()
   

    def __str__(self):
        return self.body
