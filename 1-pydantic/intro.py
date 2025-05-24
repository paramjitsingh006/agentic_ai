from typing import List
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    hobbies: List[str] = []

user = User(name='John', age=22)
print(user)
