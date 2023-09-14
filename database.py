from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

# postgresql://username:password@host:port/database_name
engine = create_engine(DATABASE_URL)

SessionManager = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()