import os
from pydantic import BaseModel
from app.config import Config
from app.utils import load_json

class User(BaseModel):
    id: int
    name: str
    email: str

def load_users():
    base_path = Config.get_data_path()
    file_path = base_path + "/users.json"
    data = load_json(file_path)
    return [User(**item) for item in data]

def get_user_emails():
    users = load_users()
    return [u.email for u in users]
