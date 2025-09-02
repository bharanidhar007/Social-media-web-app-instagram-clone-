
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: return True
        return obj.author == request.user
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('author').prefetch_related('likes')
    serializer_class = PostSerializer; permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer): serializer.save(author=self.request.user)
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object(); user = request.user
        if user in post.likes.all(): post.likes.remove(user); return Response({'status':'unliked'})
        post.likes.add(user); return Response({'status':'liked'})
    @action(detail=True, methods=['get','post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def comments(self, request, pk=None):
        post = self.get_object()
        if request.method == 'GET':
            qs = post.comments.all(); serializer = CommentSerializer(qs, many=True); return Response(serializer.data)
        serializer = CommentSerializer(data=request.data); serializer.is_valid(raise_exception=True); serializer.save(author=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all(); serializer_class = CommentSerializer; permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer): raise NotImplementedError("Use /posts/<id>/comments/")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.author and request.user != instance.post.author:
            return Response({'detail':'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance); return Response(status=status.HTTP_204_NO_CONTENT)
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        following_ids = list(request.user.following_set.values_list('following_id', flat=True))
        qs = Post.objects.filter(author_id__in=following_ids).order_by('-created_at')
        from rest_framework.pagination import PageNumberPagination
        paginator = PageNumberPagination()
        paginated = paginator.paginate_queryset(qs, request, view=self)
        ser = PostSerializer(paginated, many=True, context={'request': request})
        return paginator.get_paginated_response(ser.data)
