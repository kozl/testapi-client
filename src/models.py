from typing import List, Optional
from enum import Enum
from datetime import date

from pydantic import BaseModel


class Status(str, Enum):
    ok = 'OK'
    not_found = 'Not found'
    error = 'Error'


class Permission(BaseModel):
    id: int
    permission: str


class UserInfoResponse(BaseModel):
    status: Status
    active: Optional[str]
    blocked: Optional[bool]
    created_at: Optional[date]
    id: Optional[int]
    name: Optional[str]
    permissions: Optional[List[Permission]]


class AuthResponse(BaseModel):
    status: Status
    token: Optional[str]\



class UpdateRequest(BaseModel):
    active: str
    blocked: bool
    name: str
    permissions: List[Permission]


class UpdateResponse(BaseModel):
    status: Status
