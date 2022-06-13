from django.db import models

class Message(models.Model):
    receiver = models.CharField(max_length=50) #받는이
    sender = models.CharField(max_length=50) #보내는이
    date = models.DateTimeField() #날짜
    text=models.TextField("쪽지")

    def summary(self):
        return self.body[:100]
