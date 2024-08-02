from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100)
    content1 = models.TextField()
    content2 = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
