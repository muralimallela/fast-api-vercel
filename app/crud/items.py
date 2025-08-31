from sqlalchemy.orm import Session
from app import models, schemas

def create_item(db: Session, item: schemas.item.ItemCreate, user_id: int):
    db_item = models.item.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
