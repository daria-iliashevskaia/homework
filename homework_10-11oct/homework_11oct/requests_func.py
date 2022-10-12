from utils import *


def all_ads(cursor):
    """
    Вывод всех объявлений с именами авторов
    """

    request = """SELECT author.name_author, description
                 FROM ads
                 JOIN author ON ads.fk_author = author.id_author"""
    create_req(cursor, request)

# вывод всех объявлений конкретных авторов
# request = """SELECT author.name_author, description
#              FROM ads
#              JOIN author ON ads.fk_author = author.id_author
#              WHERE name_author='Борис'"""
# create_req(cursor, request)

# вывод всех объявлений в диапазоне цены
# request = """SELECT author.name_author, price, description
#              FROM ads
#              JOIN author ON ads.fk_author = author.id_author
#              WHERE price<500 AND price>100
#              ORDER BY price"""
# create_req(cursor, request)

# вывод всех объявлений для конкретного города
# request = """SELECT author.name_author, price, description, address
#              FROM ads
#              JOIN address ON ads.fk_adress = address.id_address
#              JOIN author ON ads.fk_author = author.id_author
#              WHERE address.city LIKE '%Москва%'
#              """
# create_req(cursor, request)

# вывод всех объявлений для определённого пользователя и цены
# request = """SELECT author.name_author, price, description, address
#              FROM ads
#              JOIN address ON ads.fk_adress = address.id_address
#              JOIN author ON ads.fk_author = author.id_author
#              WHERE (price<500 AND price>100) AND name_author='Борис'
#              """
# create_req(cursor, request)