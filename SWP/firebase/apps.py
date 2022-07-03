import logging
from django.apps import AppConfig
from firebase import firebase


class FirebaseAppConfig(AppConfig):
    name = "firebase"

    def ready(self):
        # logging.info("Firebase: Initializing")
        print("Firebase: Initializing")
        firebase.initialize()
        firebase.db.child('signal').push({'status': 'successfully'})
        print("Firebase: Firebase module initialized successfully")
        # logging.info("Firebase: Firebase module initialized successfully")
