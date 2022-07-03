from django.db import models
import json


class FirebaseModel(models.Model):
    id = models.AutoField(serialize=False, primary_key=True)

    def save(self, *args, **kwargs):
        from firebase.firebase import db

        if not hasattr(self, '__serializer__'):
            raise KeyError('Firebase model should have __serializer__ field to be synced with database')
        if not hasattr(self, '__fbpath__'):
            raise KeyError('Firebase model should have __fbpath__ field to be synced with database')

        serializer = getattr(self, '__serializer__')
        path = getattr(self, '__fbpath__')
        print('UPD:', '/'.join(map(str, path)), serializer(instance=self).data)

        db.update({
            '/'.join(map(str, path)): serializer(instance=self).data,
        })
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        from firebase.firebase import db

        if not hasattr(self, '__fbpath__'):
            raise KeyError('Firebase model should have __fbpath__ field to be synced with database')

        path = getattr(self, '__fbpath__')
        child = db

        for entry in map(str, path):
            child = child.child(entry)

        child.remove()
        super().delete(*args, **kwargs)