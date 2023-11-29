from sqlalchemy import Column, Integer, String
from database import Base

class Image(Base):
    __tablename__ = 'tbl_image'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

