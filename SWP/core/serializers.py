from rest_framework.serializers import ModelSerializer

from core.models import Message, Chat


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
