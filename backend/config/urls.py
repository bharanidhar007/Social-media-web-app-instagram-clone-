
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, CommentViewSet, FeedView
from users.views import RegisterView, MeProfileView, PublicProfileView, FollowToggleView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('api/auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('api/profiles/me/', MeProfileView.as_view(), name='me-profile'),
    path('api/profiles/<str:username>/', PublicProfileView.as_view(), name='public-profile'),
    path('api/profiles/<str:username>/follow/', FollowToggleView.as_view(), name='follow-toggle'),
    path('api/feed/', FeedView.as_view(), name='feed'),
    path('api/', include(router.urls)),
]
