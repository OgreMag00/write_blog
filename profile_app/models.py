from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Text_post(models.Model):
    title = models.CharField(max_length=30, default=' ')
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, default='None')
    
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published_date
    
    def create_post(self, title, content, username):
        self.title = title
        self.content = content
        self.username = username
        self.save()
        
    def delete_post(self):
        self.delete()