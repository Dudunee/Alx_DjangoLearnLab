from rest_framework import viewsets, permissions, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import generics, permissions

@api_view(['POST'])
@permissions.IsAuthenticated
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        Notification.objects.create(
            recipient=post.author, 
            actor=request.user,
            verb='liked your post',
            target=post
        )
        return Response({"message": "Post liked."}, status=201)
    
    return Response({"message": "You already liked this post."}, status=400)

@api_view(['POST'])
@permissions.IsAuthenticated
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked."}, status=204)
    except Like.DoesNotExist:
        return Response({"message": "You haven't liked this post."}, status=400)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

User = get_user_model()

class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer 

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all() 
        return Post.objects.filter(author__in=following_users).order_by('-created_at') 