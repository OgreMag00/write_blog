from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Text_post(models.Model):
    title = models.CharField(max_length=30, default=' ')
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20, default='None')
    rating_like = models.PositiveIntegerField(default=0)
    rating_dislike = models.PositiveIntegerField(default=0)
    was_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published_date
    
    def create_post(self, title, content, username, was_published):
        self.title = title
        self.content = content
        self.username = username
        self.was_published = was_published
        self.save()
        
    def like(self):
        self.rating_like += 1
        self.save()
    
    def dislike(self):
        self.rating_dislike += 1
        self.save()
        
    def was_pub(self):
        self.was_published = True
        self.save()
        
    def to_draft(self):
        self.was_published = False
        self.save(update_fields=["was_published"])
        
    def change(self, title, content):
        self.title = title
        self.content = content
        self.save(update_fields=["title","content"])
        
    def delete_post(self):
        self.delete()