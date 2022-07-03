from typing import Dict

from firebase.firebase import db


def push(name: str, value: any):
    db.child(name).push(value)


def get(path: str):
    return db.child(path).get()


def update(data: Dict):
    db.update(data)
