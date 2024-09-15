from django.urls import path
from .views import (
    register, profile, user_login, user_logout,
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView,
    add_comment_to_post, edit_comment, delete_comment
)

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add-comment'),
    path('post/<int:post_pk>/comment/<int:pk>/edit/', edit_comment, name='edit-comment'),
    path('post/<int:post_pk>/comment/<int:pk>/delete/', delete_comment, name='delete-comment'),
]
