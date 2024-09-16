from django_ratelimit.decorators import ratelimit
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, permissions
from .models import FriendRequest
from .serializers import FriendRequestSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email').lower()
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        keyword = self.request.query_params.get('q', '')
        if not keyword:
            return User.objects.none()
        
        # Search by exact email or partial name
        queryset = User.objects.filter(
            Q(email__iexact=keyword) | Q(name__icontains=keyword)
        )
        return queryset


class SendFriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    @ratelimit(key='user', rate='3/m', method='ALL', block=True)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UpdateFriendRequestView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = FriendRequest.objects.get(id=self.kwargs['pk'])
        if obj.receiver != self.request.user:
            raise PermissionDenied("You do not have permission to modify this request.")
        return obj

class ListFriendsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(sender=self.request.user, status='accepted')

class ListPendingRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(receiver=self.request.user, status='pending')
