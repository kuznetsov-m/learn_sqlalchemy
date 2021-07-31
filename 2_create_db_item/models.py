from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, Date, DateTime, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class Candels(Base):
    __tablename__ = 'candels'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    value = Column(Float, nullable=True)

    # def __init__(self, value):
    #     self.open = open
    #     self.close = close
    #     self.high = high
    #     self.low = low
    #     self.value = value
    #     self.volume = volume
    #     self.begin = begin
    #     self.end = end

class Model(Base):
    __tablename__ = 'models'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    tiker = Column(String, nullable=False)
