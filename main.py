from fastapi import FastAPI, HTTPException, Depends, Path
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionManager
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PersonBase(BaseModel):
    name: str

def get_db():
    db = SessionManager()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

#Creating the endpoint to add a new person
@app.post("/api")
async def create_person(person: PersonBase, db: db_dependency):
    db_person = models.Persons(name=person.name)
    db.add(db_person)
    db.commit()
    
@app.get('/api/{user_id}')
async def get_person(db: db_dependency, user_id: int | str = Path(title="The ID or name of the user")):
    if user_id.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user_id)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user_id).first()
    

    if not person:
        raise HTTPException(status_code=404, detail="user not available")
    
    return person

@app.patch("/api/{user_id}")
async def update_person(updated_person: PersonBase,   db: db_dependency, user_id:int |str = Path(title="The ID or name of the user")):
    if user_id.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user_id)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user_id).first()

    if not person:
        raise HTTPException(status_code=404, detail="user not available")
    
    person.name = updated_person.name
    db.commit()

@app.delete("/api/{user_id}")
async def deleter_person(db:db_dependency, user_id:int |str = Path(title="The ID or name of the user")):
    if user_id.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user_id)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user_id).first()

    if not person:
        raise HTTPException(status_code=404, detail="user not available")
    
    db.delete(person)
    db.commit()
