from django_filters import rest_framework as filters

from core.models import Message, Chat


class MessageFilter(filters.FilterSet):
    class Meta:
        model = Message
        fields = "__all__"

class ChatFilter(filters.FilterSet):
    class Meta:
        model = Chat
        fields = "__all__"