from pydantic import BaseModel
from typing import Literal

UserRole = Literal[
    "admin",
    "medical",
    "forensic",
    "researcher",
    "auditor"
]

class User(BaseModel):
    username: str
    role: UserRole
