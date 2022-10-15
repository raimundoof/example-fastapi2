from app import oauth2
from .. import models, schemas, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func 
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

#@router.get("/", response_model=List[schemas.Post])

#@router.get("/")

@router.get("/", response_model=List[schemas.PostOut])
#def get_posts():
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
limit: int= 10, skip: int = 0, search: Optional[str] = ""): 

    print(search)
  #  cursor.execute("""SELECT * from posts """)
   # posts = cursor.fetchall()
   #posts = db.query(models.Post).filter(models.Post.owner_id==current_user.id).all()
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
   
    posts = db.query(models.Post, func.count(models.Vote.posts_id).label("votes")).join(models.Vote, models.Vote.posts_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #print(results)
   
   
   
    #return results
    return posts
   #  return {"data": posts}

@router.get("/{id}", response_model=schemas.PostOut)
#def get_post(id: int, response: Response):
#def get_post(id: int, db: Session = Depends(get_db)):
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#def get_post(id: int):  
   # cursor.execute("""SELECT * from posts WHERE id = %s """, (str(id),))
    #post = cursor.fetchone()
    #test_post = cursor.fetchone() 
    #print(test_post)
    #post = find_post(int(id))

   # post = db.query(models.Post).filter(models.Post.id == id).first()

    post = db.query(models.Post, func.count(models.Vote.posts_id).label("votes")).join(models.Vote, models.Vote.posts_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    



    #print(post)

    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"Post with id: {id} was not found.")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"Post with id: {id} was not found."}
    #return {"post_detail": post}
    
  #  if post.owner_id != current_user.id:
   #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail = "Not authorized to perform requested action.")
   
    
    
    return post



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
#def create_posts(post: schemas.PostCreate,db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
def create_posts(post: schemas.PostCreate,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
  
   #post_dict = post.dict()
   #post_dict['id'] = randrange(0, 1000000)
   #posts.append(post_dict)
   # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING
  #  * """,
  #                  (post.title, post.content, post.published))
   # new_post = cursor.fetchone()
    
   # return{"data": post_dict}

    #conn.commit()
    
    #print(**post.dict())
    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
    #print(current_user.id)
    #print(current_user.email)
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    #return {"data": new_post}
    return new_post
  


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)

 #  cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id),))
 #   deleted_post = cursor.fetchone()
 #   conn.commit()
    
    #index = find_index_post(id)

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
   # if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist.")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail = "Not authorized to perform requested action.")
   
    post_query.delete(synchronize_session=False)
    db.commit()

    #if index == None:
     #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
      #                      detail=f"Post with id: {id} does not exist.")

    #my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
 #   cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id),))
    
  #  updated_post = cursor.fetchone()
  #  conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} does not exist.")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail = "Not authorized to perform requested action.")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    # post_query.update({'title': 'hey this is my updated title', 'content': 'this is my updated content'}, synchronize_session=False)

    db.commit()

    #return {"data": post_query.first()}
    return post_query.first()
   # return {"data": 'successfull'}
    #index = find_index_post(id)

    #if index == None:
    #        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                        detail=f"Post with id: {id} does not exist.")
    
    #post_dict = post.dict()
    #post_dict['id'] = id
    #my_posts[index] = post_dict
    #return {"data": post_dict}

