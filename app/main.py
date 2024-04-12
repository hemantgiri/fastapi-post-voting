from fastapi import FastAPI, status, HTTPException,Depends
from datetime import datetime
from . import models, schemas, utils
from .database import engine, get_db
from .routers import user, post, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



# @app.get("/posts")
# def get_posts():
#      cursor.execute("""SELECT * FROM posts""")
#      posts = cursor.fetchall()
#      return {"data" : posts}


# @app.post("/post" , status_code=status.HTTP_201_CREATED) 
# def create_post(post : Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))    
#     conn.commit()
#     new_post = cursor.fetchone()
#     return {"data": "new_post"}


# @app.get("/post/{id}")
# def get_post(id : int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s """,(str(id)))    
#     test_post= cursor.fetchone()
#     if not test_post:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
#     return {"data": test_post}



# @app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))    
#     conn.commit()
#     deleted_post= cursor.fetchone()
#     if not deleted_post:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
#     return {"data": deleted_post}



# @app.put("/post/{id}") 
# def create_post(post : Post):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s) WHERE id = %s RETURNING *""",(post.title, post.content, post.published, str(id)))    
#     conn.commit()
#     updated_post = cursor.fetchone()
#     if not updated_post:
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
#     return {"data": updated_post}







