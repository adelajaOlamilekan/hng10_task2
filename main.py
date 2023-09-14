from fastapi import FastAPI, Depends, Path
from fastapi.dependencies.utils import Annotated
import models
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionManager, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionManager()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

#Creating the endpoint to add a new person
@app.post("/api")
async def create_person(person: schemas.PersonBase, db: db_dependency):
    crud.create_person(db=db, person=person)

    
@app.get('/api/{user}')
async def get_person(db: db_dependency, user):
    crud.get_person(db=db, user=user)

@app.patch("/api/{user}")
async def update_person(updated_person: schemas.PersonBase,   db: db_dependency, user):
    crud.update_person(updated_person=updated_person, db=db, user=user)

@app.delete("/api/{user}")
async def delete_person(db:db_dependency, user):
    crud.delete_person(db=db, user=user)