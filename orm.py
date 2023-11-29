from sqlalchemy import Column , Integer ,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Image(Base):
    __tablename__="Image"

    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    image_name=Column(String(256))
    image_path=Column(String(256))


    def __repr__(self):
        return f"Image(id={self.id}, image_name={self.image_name}, image_path={self.image_path})"