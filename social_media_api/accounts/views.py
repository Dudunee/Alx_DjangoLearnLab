# accounts/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import UserSerializer, UserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(UserLoginView, self).post(request, *args, **kwargs)
        token = response.data['token']
        user = CustomUser.objects.get(auth_token=token)
        return Response({
            'token': token,
            'user': UserSerializer(user).data
        })

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


User = get_user_model()

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({"message": "Following user."})

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({"message": "Unfollowed user."})