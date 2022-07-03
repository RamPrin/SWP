from pyrebase import pyrebase
import json
import os

fireapp, db = None, None


def initialize():
    global db, fireapp
    with open(os.path.join(*['SWP', 'firebase', 'credentials.json']), 'r') as credential_file:
        fireapp = pyrebase.initialize_app(json.load(credential_file))
    db = fireapp.database()

