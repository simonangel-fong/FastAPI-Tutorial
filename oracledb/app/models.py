from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class TestTable(Base):
    __tablename__ = 'test_table'

    id = Column(Integer, primary_key=True,
                server_default=Identity(start=1, increment=1))
    test_column = Column(String(50), unique=True, nullable=False)
