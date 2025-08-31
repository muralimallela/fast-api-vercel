from sqlalchemy.orm import Session
from app import models, schemas
from app.services.security import hash_password

def get_user_by_username(db: Session, username: str):
    return db.query(models.user.User).filter(models.user.User.username == username).first()

def create_user(db: Session, user: schemas.user.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.user.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
