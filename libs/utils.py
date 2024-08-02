from uuid import uuid4
from datetime import datetime


def now():
    return datetime.now()


def generate_id():
    id = str(uuid4())
    return id