from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

DATABASE_URL = str(os.getenv("DATABASE_URL"))
print(os.getenv("DATABASE_URL"))

#Create the database engine
engine = create_engine(DATABASE_URL)

#Create the database manipulation session
SessionManager = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()