from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# Create a connection to the database
Database_URL = 'sqlite:///database.db'
# 
engine = create_engine(Database_URL, connect_args={'check_same_thread': False})

# Create a session
Session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()