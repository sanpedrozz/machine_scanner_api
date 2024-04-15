# models.py

from pydantic import BaseModel
from typing import Union


class PortDescription(BaseModel):
    description: str = 'com0com'


class SendMessageRequest(BaseModel):
    id: Union[int, str]
