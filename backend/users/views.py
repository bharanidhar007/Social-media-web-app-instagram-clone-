
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, ProfileSerializer, PublicProfileSerializer
from .models import Follow
class RegisterView(generics.CreateAPIView): queryset = User.objects.all(); serializer_class = RegisterSerializer; permission_classes = [permissions.AllowAny]
class MeProfileView(generics.RetrieveUpdateAPIView): serializer_class = ProfileSerializer; permission_classes = [permissions.IsAuthenticated]
def get_object(self): return self.request.user.profile
class PublicProfileView(generics.RetrieveAPIView): serializer_class = PublicProfileSerializer; permission_classes = [permissions.AllowAny]
def get_object(self): username = self.kwargs['username']; user = get_object_or_404(User, username=username); return user.profile
class FollowToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, username):
        target_user = get_object_or_404(User, username=username)
        if target_user == request.user:
            return Response({'detail':'Cannot follow yourself.'}, status=400)
        follow, created = Follow.objects.get_or_create(follower=request.user, following=target_user)
        if not created: follow.delete(); return Response({'status':'unfollowed'})
        return Response({'status':'followed'})
