from email.policy import default
from sqlalchemy import Column, ForeignKey, Boolean, Float, Integer, String, Date, func, or_, and_
from sqlalchemy.orm import relationship, object_session
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
import datetime as dt

from sqlalchemy.sql.sqltypes import VARCHAR

from app import utils
from app.db.base import Base
from enum import IntEnum


class Organisation(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    postcode = Column(String)
    contact_name = Column(String)
    contact_phone = Column(String)
    contact_email = Column(String)
    departments = Column(Integer, default = 0)
    sqlite_autoincrement=True


