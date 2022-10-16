from DB_create import *


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
        # (этот блок кода пригодится только если таблицы не заполнены)

        # insert_breeds_info(cursor)
        # insert_type_info(cursor)
        # insert_colour_info(cursor)
        # insert_outcome_subtype_info(cursor)
        # insert_outcome_type_info(cursor)
        # insert_animal_info(cursor)
        # insert_shelter_info(cursor)

        # создаю новых пользователей с разными правами

        # user(cursor, "SELECT", "user1")
        # user(cursor, "UPDATE, INSERT", "user_updater")

        cursor.close()

    connection.close()


if __name__ == "__main__":
    main()
