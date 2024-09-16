from django.urls import path
from .views import SignupView, LoginView, UserSearchView, SendFriendRequestView, UpdateFriendRequestView, ListFriendsView, ListPendingRequestsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('send-request/', SendFriendRequestView.as_view(), name='send-request'),
    path('update-request/<int:pk>/', UpdateFriendRequestView.as_view(), name='update-request'),
    path('friends/', ListFriendsView.as_view(), name='list-friends'),
    path('pending-requests/', ListPendingRequestsView.as_view(), name='pending-requests'),    
]
