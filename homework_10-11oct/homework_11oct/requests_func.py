from utils import *


def all_ads(cursor):
    """
    Вывод всех объявлений с именами авторов
    """

    request = """SELECT author.name_author, description
                 FROM ads
                 JOIN author ON ads.fk_author = author.id_author"""
    create_req(cursor, request)


def author_choice(cursor, author_name: str):
    """
    Вывод всех объявлений конкретных авторов
    """

    request = f"""SELECT author.name_author, description
                 FROM ads
                 JOIN author ON ads.fk_author = author.id_author
                 WHERE name_author= '{author_name}'"""
    create_req(cursor, request)


def price_choice(cursor, int_from: int, int_to: int):
    """
    Вывод всех объявлений в диапазоне цены, сортировка по возрастанию цены
    """

    request = f"""SELECT author.name_author, price, description
                 FROM ads
                 JOIN author ON ads.fk_author = author.id_author
                 WHERE price<{int_to} AND price>{int_from}
                 ORDER BY price"""
    create_req(cursor, request)


def city_choice(cursor, city: str):
    """
    Вывод всех объявлений для конкретного города
    """

    request = f"""SELECT author.name_author, price, description, address
                 FROM ads
                 JOIN address ON ads.fk_adress = address.id_address
                 JOIN author ON ads.fk_author = author.id_author
                 WHERE address.city LIKE '%{city}%'
                 """
    create_req(cursor, request)


def author_price(cursor, author_name: str, int_from: int, int_to: int):
    """
    Вывод всех объявлений для определённого пользователя и цены
    """

    request = f"""SELECT author.name_author, price, description, address
                 FROM ads
                 JOIN address ON ads.fk_adress = address.id_address
                 JOIN author ON ads.fk_author = author.id_author
                 WHERE (price<{int_to} AND price>{int_from}) AND name_author='{author_name}'
                 """
    create_req(cursor, request)
