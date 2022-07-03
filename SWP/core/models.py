from django.db import models
from rest_framework.serializers import ModelSerializer
from firebase.models import FirebaseModel
from django.utils import timezone


class Chat (models.Model):
    class Meta:
        db_table = 'chats'

    id = models.BigAutoField(serialize=True, primary_key=True)


class Message (FirebaseModel):
    class Meta:
        db_table = 'messages'

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(unique=True, auto_now=True)
    text = models.TextField()

    def save(self, *args, **kwargs):
        self.timestamp = timezone.now()
        super().save(*args, **kwargs)

    @property
    def __serializer__(self):
        class MessageSerializer(ModelSerializer):
            class Meta:
                model = Message
                fields = '__all__'
        return MessageSerializer

    @property
    def __fbpath__(self):
        return ['chats', self.chat.id, int(self.timestamp.timestamp() * 10000)]
