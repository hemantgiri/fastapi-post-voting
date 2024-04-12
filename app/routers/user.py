from .. import models, schemas, utils
from fastapi import FastAPI, status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(tags=['users'])

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate , db : Session = Depends(get_db)):
    # new_post = models.Post(title = post.title, content = post.content, published = post.published)
    user.password = utils.get_password_hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/user/{id}", status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def get_user(id: int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    return user