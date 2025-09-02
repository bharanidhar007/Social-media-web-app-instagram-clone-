
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    class Meta: model = User; fields = ('username','email','password')
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data.get('email',''), password=validated_data['password'])
        return user
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta: model = Profile; fields = ('username','bio','avatar'); read_only_fields=('username',)
class PublicProfileSerializer(ProfileSerializer):
    followers = serializers.SerializerMethodField(); following = serializers.SerializerMethodField()
    class Meta(ProfileSerializer.Meta): fields = ProfileSerializer.Meta.fields + ('followers','following',)
    def get_followers(self,obj): return obj.user.followers_set.count()
    def get_following(self,obj): return obj.user.following_set.count()
