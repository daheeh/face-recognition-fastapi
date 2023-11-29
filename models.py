from sqlalchemy import Column, Integer, Text
from database import Base

class Image(Base):
    __tablename__ = 'Image'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
