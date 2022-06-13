from django.db import models

class staticBlog(models.Model):
    subject = models.CharField(max_length = 200)
    drafter = models.CharField(max_length = 100)
    date = models.DateTimeField()
    textBody = models.TextField()

    def __str__(self_):
        return self.name
    
    def summary(self):
        return self.textBody[:100]
