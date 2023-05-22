from dotenv.main import load_dotenv
import os
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

# функция подключения к базе данных book
def connect_db():
    load_dotenv()
    password = os.environ['password']
    DSN = f'postgresql://postgres:{password}@localhost:5432/books'
    engine = sq.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine