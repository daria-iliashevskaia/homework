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
                                      database="postgres")
        connection.autocommit = True
        return connection

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def create_req(cursor, request):
    """
    Создаёт запрос к БД и выводит результат
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