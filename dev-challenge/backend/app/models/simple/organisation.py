from app import schemas
from .base import Base
from typing import List


class Organisation(Base):
    id : int = None
    name : str = None
    address: str = None
    postcode: str = None
    contact_name: str = None
    contact_phone: str = None
    contact_email: str = None
    departments: int = None



