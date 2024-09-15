from django.urls import path
from .views import (
    UserProfileView, 
    BlogPostListView, 
    BlogPostDetailView, 
    BlogPostCreateView, 
    BlogPostUpdateView, 
    BlogPostDeleteView,
    UserRegistrationView,
    UserLoginView,
    UserLogoutView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('posts/', BlogPostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('posts/new/', BlogPostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post-delete'),
]
