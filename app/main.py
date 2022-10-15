#Testes com FastAPI

from ctypes.wintypes import HACCEL
import imp
from multiprocessing import synchronize
from poplib import CR
import re

from secrets import randbelow
#from typing import Optional, List
#from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi import FastAPI
#from fastapi.params import Body
#from pydantic import BaseModel
#from passlib.context import CryptContext
#from random import randrange
#import psycopg2
#from psycopg2.extras import RealDictCursor
#import time
#from sqlalchemy.orm import Session
#from sqlalchemy.sql.functions import mode
#from . import models, schemas, utils
from . import models
#from .database import engine, SessionLocal
#from .database import engine, get_db
from .database import engine
#import tkinter as tk
from .routers import post, user, auth, vote
from .config import settings

from app import database



#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#models.Base.metadata.create_all(bind=engine)


app=FastAPI()

# Dependency
#def get_db():
 #   db = SessionLocal()
  #  try:
   #     yield db
    #finally:
     #   db.close()

#class Post(BaseModel):
 #   title: str
  #  content: str
   # published: bool = True

#while True:

 #   try:
  #      conn = psycopg2.connect(host='localhost', database='fastapi',user='postgres', password='postgres', cursor_factory=RealDictCursor)
   #     cursor = conn.cursor()
    #    print("Database connection was sucessfull.")
     #   break
   # except Exception as error:
    #    print("Connection to Database failed.")
     #   print("Error: ", error)
      #  time.sleep(2)

#my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1 },
#{"title": "favorite foods", "contents": "I like tomate", "id": 2}]

#def find_post(id):
 #   for p in my_posts:
  #      if p['id'] == id:
   #         return p

#def find_index_post(id):
 #   for i, p in enumerate(my_posts):
  #      if p['id'] == id:
   #         return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World2"}

#@app.get("/sqlalchemy")
#def test_posts(db: Session = Depends(get_db)):
    
 #   posts = db.query(models.Post).all()
    
    #return{"Status": "Sucess"}
  #  return {"data": posts}




#@app.get("/posts/latest")
#def get_latest_post():
 #   post = my_posts[len(my_posts) - 1]
  #  #return {"detail": post}
   # return post



