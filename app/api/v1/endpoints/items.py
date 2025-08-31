from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import crud, schemas
from .users import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.item.ItemOut)
def create_item(item: schemas.item.ItemCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.items.create_item(db, item, current_user.id)
