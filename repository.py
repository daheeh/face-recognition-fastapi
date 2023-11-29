from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from orm import Image

def get_img(session: Session) -> List[Image]:
    return session.query(Image).all()
   # return session.execute(select(Img)).scalars().all()


def create_img(db, image_name: str, image_path: str):
    db_img = Image(img_name=image_name, img_path=image_path)
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img