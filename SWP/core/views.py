from django.shortcuts import render
from rest_framework import mixins
from django_filters import rest_framework as filters
from rest_framework.generics import GenericAPIView

from core.filters import MessageFilter, ChatFilter
from core.models import Message, Chat
from core.serializers import MessageSerializer, ChatSerializer


def front(request):
    context = {}
    return render(request, "index.html", context)


class MessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MessageFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ChatViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ChatFilter

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)