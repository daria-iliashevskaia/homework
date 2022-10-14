import psycopg2
from psycopg2 import Error


def connect_bd():
    """
    Подключает к PGadmin с уже созданной БД
    """

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="19IDD93a",
                                      host="127.0.0.1",
                                      port="5432",
                                      database='shelter')
        connection.autocommit = True
        return connection

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def create_db(cursor, name_db: str):
    """
    Создаёт базу данных с указанным названием
    """
    try:
        sql_create_database = f'create database {name_db}'
        cursor.execute(sql_create_database)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def create_req(cursor, request: str):

    """
    Функция для выполнения запросов и вывода информации.
    Создаёт запрос к БД и выводит результат.
    """

    try:
        cursor.execute(request)

        while True:
            record = cursor.fetchone()
            if record:
                print(f"{record}\n")
            else:
                break

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def create_breed_table(cursor):

    """
    Создаёт таблицу с нужным названием
    """

    request = """CREATE TABLE IF NOT EXISTS breed_dict(
                id_breed INTEGER PRIMARY KEY,
                name_breed VARCHAR (40) NOT NULL
                ) 
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица breed_dict не создана", error)


def create_type_table(cursor):

    """
    Создаёт таблицу с нужным названием
    """

    request = """CREATE TABLE IF NOT EXISTS type_dict(
                id_type INTEGER PRIMARY KEY,
                name_type VARCHAR (40) NOT NULL
                ) 
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица type_dict не создана", error)


def create_colour_table(cursor):

    """
    Создаёт таблицу с нужным названием
    """

    request = """CREATE TABLE IF NOT EXISTS colour_dict(
                id_colour INTEGER PRIMARY KEY,
                name_colour VARCHAR (40) NOT NULL
                ) 
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица colour_dict не создана", error)


def create_outcome_subtype_table(cursor):

    """
    Создаёт таблицу с нужным названием
    """

    request = """CREATE TABLE IF NOT EXISTS outcome_subtype(
                id_outcome_subtype INTEGER PRIMARY KEY,
                name_outcome_subtype VARCHAR (40) NOT NULL
                ) 
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица outcome_subtype не создана", error)


def create_outcome_type_table(cursor):

    """
    Создаёт таблицу с нужным названием
    """

    request = """CREATE TABLE IF NOT EXISTS outcome_type(
                id_outcome_type INTEGER PRIMARY KEY,
                name_outcome_type VARCHAR (40) NOT NULL
                ) 
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица outcome_type не создана", error)


def create_animal_table(cursor):

    """
    Создаёт таблицу с animal_dict
    """

    request = """CREATE TABLE IF NOT EXISTS animal_dict(
                animal_id VARCHAR(20) PRIMARY KEY,
                fk_type INTEGER,
                animal_name VARCHAR(20),
                fk_breed INTEGER,
                fk_colour_1 INTEGER,
                fk_colour_2 INTEGER,
                date_of_birth TIMESTAMP,
                    FOREIGN KEY (fk_type) REFERENCES type_dict(id_type),
                    FOREIGN KEY (fk_breed) REFERENCES breed_dict(id_breed),
                    FOREIGN KEY (fk_colour_1) REFERENCES colour_dict(id_colour),
                    FOREIGN KEY (fk_colour_2) REFERENCES colour_dict(id_colour)                                                 
                ) 
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица animal_dict не создана", error)


def create_shelter_table(cursor):

    """
    Создаёт таблицу shelter_info
    """

    request = """CREATE TABLE IF NOT EXISTS shelter_info(
                index INTEGER PRIMARY KEY,
                fk_animal_id VARCHAR(20),
                fk_outcome_subtype INTEGER,
                fk_outcome_type INTEGER,
                outcome_month INTEGER,
                outcome_year INTEGER,
                age_upon_outcome VARCHAR(40),
                    FOREIGN KEY (fk_animal_id) REFERENCES animal_dict(animal_id),
                    FOREIGN KEY (fk_outcome_subtype) REFERENCES outcome_subtype(id_outcome_subtype),
                    FOREIGN KEY (fk_outcome_type) REFERENCES outcome_type(id_outcome_type)                                   
                ) 
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица shelter_info не создана", error)


def insert_breeds_info(cursor):

    """
    Заполняет таблицу breed_dict информацией из файла breed_dict.csv
    """

    request = """INSERT INTO breed_dict(id_breed, name_breed)
                 VALUES (''), (''), ('')
                """
    try:
        cursor.execute(request)
    except (Exception, Error) as error:
        print("Таблица shelter_info не создана", error)