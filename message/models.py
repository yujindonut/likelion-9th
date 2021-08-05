from django.db import models
from django.contrib.auth.models import User
    
# Create your models here.
class Message(models.Model):
    to = models.CharField(max_length=50)
    writer = models.CharField(max_length=50) 
    pub_date=models.DateTimeField()
    body=models.TextField("쪽지")
    CustomUser = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, null=False)
    
    def summary(self):
        return self.body[:80]
'''
class Reply(models.Model):
    messageId = models.ForeignKey("FirstMessage",on_delete=models.CASCADE,db_column="messageId")
    comment_id = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    
    writer = models.CharField(max_length=50)
    body = models.TextField('답장')
    pub_date=models.DateTimeField()'''