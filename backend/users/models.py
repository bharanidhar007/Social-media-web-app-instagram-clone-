
from django.db import models
from django.contrib.auth.models import User
def user_avatar_upload(instance, filename):
    return f"avatars/{instance.user.username}/{filename}"
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=280, blank=True)
    avatar = models.ImageField(upload_to=user_avatar_upload, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Profile({self.user.username})"
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_set')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers_set')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: unique_together = ('follower', 'following')
