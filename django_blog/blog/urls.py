from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    register, profile, user_login, user_logout, search
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Updated path
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Updated path
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # Updated path
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', search, name='search'),
    path('tags/<str:tag_name>/', PostListView.as_view(), name='tagged-posts'),
    path('tags/<str:tag_name>/', tagged_posts, name='tagged-posts'),
]
