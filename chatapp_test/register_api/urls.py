from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI,OnlineUsersAPIView, ChatStartAPI
from .suggest_view import SuggestedFriendsAPI

from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/online-users/', OnlineUsersAPIView.as_view(), name='online-users'),
    path('api/chat/start/', ChatStartAPI.as_view(), name='chat-start'),
    path('api/chat/start/<int:id>/', ChatStartAPI.as_view(), name='chat-start-recipient'),
    path('api/suggested-friends/<int:user_id>/', SuggestedFriendsAPI.as_view(), name='suggested_friends')
]

