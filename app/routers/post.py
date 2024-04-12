from .. import models, schemas, utils, oauth2
from fastapi import FastAPI, status, HTTPException,Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(tags=['posts'])

@router.get("/posts", status_code=status.HTTP_201_CREATED,response_model=List[schemas.PostOut])
def get_posts(limit: int = 10, skip : int = 0, search : Optional[str] = "" ,db : Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id==models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return  results


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate , db : Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # new_post = models.Post(title = post.title, content = post.content, published = post.published)
    print(current_user)
    new_post = models.Post(owner_id=current_user.id,**post.model_dump())
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/post/{id}", status_code=status.HTTP_201_CREATED,response_model=schemas.PostOut)
def get_post(id: int, db : Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id==models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    return  post



@router.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db : Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    if post.owner_id!= current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/post/{id}", response_model=schemas.Post) 
def update_post(id: int, post : schemas.PostCreate, db : Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    updated_post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = updated_post_query.first()
    if not updated_post:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    if updated_post.owner_id!= current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized")
    updated_post_query.update(post.model_dump(), synchronize_session=False)
    db.commit()
    return updated_post