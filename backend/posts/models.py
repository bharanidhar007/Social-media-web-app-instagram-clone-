
from django.db import models
from django.contrib.auth.models import User
def post_image_upload(instance, filename): return f"posts/{instance.author.username}/{filename}"
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    caption = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=post_image_upload, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    class Meta: ordering = ['-created_at']
    def __str__(self): return f"Post({self.id}) by {self.author.username}"
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ['created_at']
