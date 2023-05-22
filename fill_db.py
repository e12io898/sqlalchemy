import json
from model_db import Publisher, Shop, Book, Stock, Sale
from connect import connect_db

session, engine = connect_db()

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