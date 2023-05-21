import os
from dotenv.main import load_dotenv
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from model_db import create_tables, Base, Publisher, Shop, Book, Stock, Sale

# информация о продаже по названию книги
def sale_info(test):
    q = session.query(Book, Stock, Sale, Shop, Publisher)\
        .filter(Shop.id == Stock.shop_id,
                Stock.id == Sale.stock_id,
                Publisher.id == Book.pub_id,
                Book.id == Stock.book_id).filter(Publisher.id == test)
    for i in q.all():
        print(f'{i.Book.title.ljust(40)} | '
              f'{i.Shop.shop_name.ljust(10)} | '
              f'{str(i.Sale.price).ljust(5)} | '
              f'{str(i.Sale.date_sale).ljust(10)} |')


if __name__ == '__main__':
    load_dotenv()
    password = os.environ['password']
    DSN = f'postgresql://postgres:{password}@localhost:5432/books'
    engine = sq.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Создание таблиц:
    create_tables(engine)
    # Вывод информации о продаже:
    sale_info(1)

    session.close()