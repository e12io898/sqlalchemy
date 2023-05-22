import datetime
from fill_db import fill_db
from connect import connect_db
from model_db import create_tables, Publisher, Shop, Book, Stock, Sale

# Информация о продаже по имени или id издателя
def sale_info(pub):
    query = session.query(
        Book.title, Shop.shop_name, Sale.price, Sale.date_sale).\
        select_from(Shop).\
        join(Stock, Stock.shop_id == Shop.id).\
        join(Book, Book.id == Stock.book_id).\
        join(Publisher, Publisher.id == Book.pub_id).\
        join(Sale, Sale.stock_id == Stock.id)

    print(f'{"Book": ^40} | {"Shop": ^10} | {"Price": ^8} | {"Date": ^10}')
    if pub.isdigit():
        query = query.filter(Publisher.id == pub).all()
        for book_title, shop_name, price, date_sale in query:
            print(f'{book_title: <40} | {shop_name: <10} | '
                  f'{price: < 8} | {date_sale.strftime("%d-%m-%Y")}')
    else:
        query = query.filter(Publisher.pub_name == pub).all()
        for book_title, shop_name, price, date_sale in query:
            print(f'{book_title: <40} | {shop_name: <10} | '
                  f'{price: < 8} | {date_sale.strftime("%d-%m-%Y")}')

if __name__ == '__main__':
    session, engine = connect_db()
    # Создание таблиц:
    create_tables(engine)
    # заполнение базы данных из 'tests_data.json':
    fill_db()
    # Вывод информации о продаже:
    test = input('Введите id или имя издателя: ')
    sale_info(test)

    session.close()