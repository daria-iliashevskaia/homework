from requests_func import *


def main():
    conn = connect_bd()
    if conn:

        cursor = conn.cursor()
        while True:
            print(f"Что вы выберете?\n"
                  f"1. Вывод всех объявлений с именами авторов \n"
                  f"2. Вывод всех объявлений конкретных авторов \n"
                  f"3. Вывод всех объявлений в диапазоне цены \n"
                  f"4. Вывод всех объявлений для конкретного города \n"
                  f"5. Вывод всех объявлений для определённого пользователя и цены \n"
                  f"6. Выйти из программы\n")

            user_choice = int(input("Введите ваш выбор: "))
            if user_choice == 1:
                all_ads(cursor)

            if user_choice == 2:
                author_name = input("Введите имя пользователя: ")
                author_choice(cursor, author_name)

            if user_choice == 3:
                int_from = int(input("Введите диапазон цены (в рублях). От: "))
                int_to = int(input("До: "))
                price_choice(cursor, int_from, int_to)

            if user_choice == 4:
                city = input("Введите название города: ")
                city_choice(cursor, city)

            if user_choice == 5:
                author_name = input("Введите имя пользователя: ")
                int_from = int(input("Введите диапазон цены (в рублях). От: "))
                int_to = int(input("До: "))
                author_price(cursor, author_name, int_from, int_to)

            if user_choice == 6:
                quit()
                cursor.close()
                conn.close()


if __name__ == "__main__":
    main()
