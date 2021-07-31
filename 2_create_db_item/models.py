from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, Date, DateTime, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import uuid

Base = declarative_base()

class Ticker(Base):
    __tablename__ = 'tickers'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = Column(String)

class Candel(Base):
    __tablename__ = 'candels'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    ticker_id = Column(UUID(as_uuid=True), ForeignKey(Ticker.id, ondelete='SET NULL'))
    value = Column(Float, nullable=False)

class Model(Base):
    __tablename__ = 'models'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = Column(String, nullable=False)
    ticker_id = Column(UUID(as_uuid=True), ForeignKey(Ticker.id, ondelete='SET NULL'))
