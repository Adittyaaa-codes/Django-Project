from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InstaPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ImageField(upload_to="photos/", blank=False, null=False)
    likes = models.IntegerField(default=0)
    caption = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
        self.post.delete(save=False) 
        super().delete(*args, **kwargs)  
    
    def __str__(self):
        return f'{self.user.username} - {self.caption[:8]}...'
    
class Comment(models.Model):
    post = models.ForeignKey(InstaPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} on {self.post.id}: {self.content[:30]}'
        