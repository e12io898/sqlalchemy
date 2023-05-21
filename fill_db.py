import json
from dotenv.main import load_dotenv
import os
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from model_db import Publisher, Shop, Book, Stock, Sale

load_dotenv()
password = os.environ['password']
DSN = f'postgresql://postgres:{password}@localhost:5432/books'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

# Задание 3 - наполнение бд
def fill_db():
    with open('tests_data.json', 'r', encoding='UTF-8') as data_file:
        data = json.load(data_file)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

fill_db()