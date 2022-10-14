from DB_func import *


def main():
    connection = connect_bd()
    if connection:
        cursor = connection.cursor()

        # создаю базу данных с названием "Shelter"
        # create_db(cursor, 'Shelter')

        # создаю таблицы в БД
        create_breed_table(cursor)
        create_type_table(cursor)
        create_colour_table(cursor)
        create_outcome_subtype_table(cursor)
        create_outcome_type_table(cursor)
        create_animal_table(cursor)
        create_shelter_table(cursor)

        # заполняю таблицы данными из csv файлов

        cursor.close()

    connection.close()


if __name__ == "__main__":
    main()
