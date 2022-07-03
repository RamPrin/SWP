from django.urls import path

from core.views import MessageViewSet, ChatViewSet

urlpatterns = [
    path('messages/', MessageViewSet.as_view()),
    path('chats/<pk>', ChatViewSet.as_view()),
]