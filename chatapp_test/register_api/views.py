from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import User


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response = super(LoginAPI, self).post(request, format=None)
        return Response({
            "token": response.data['token'],
            "username": user.username,
            "name": user.first_name + ' ' + user.last_name,
            "message": "Login successful"
        })
    
class OnlineUsersAPIView(APIView):
    def get(self, request):
        users = User.objects.filter(is_online=True)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    

class ChatStartAPI(APIView):
    def post(self, request, id):

        current_user_id = request.user.id
        if current_user_id == id:
            return Response({'detail': 'You cannot initiate a chat with yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            recipient = User.objects.get(id=id, is_online=True)
        except User.DoesNotExist:
            return Response({'detail': 'Recipient is offline or unavailable.'}, status=status.HTTP_404_NOT_FOUND)

        response_data = {
            'message': 'Chat initiated successfully.',
            'recipient_name': recipient.username,
            'availability': 'available to chat',
        }
        return Response(response_data, status=status.HTTP_200_OK)
    