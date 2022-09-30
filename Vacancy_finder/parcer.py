from copy import deepcopy
from classes import *
from utils import *


def main():
    key_word = input("Привет! Введите ключевое слово, по которому необходимо искать вакансии: -> ")
    print("Спасибо! Начинаем искать вакансии на HH.ru и SuperJob")
    v = Vacancy()
    print("Ищу на HH...")
    v.parse_vacancy_hh(key_word)
    print("Ищу на SuperJob...")
    v.parse_vacancy_sj(key_word)

    print(f"Список готов!\nЧто вы выберете?\n"
          f"1. Топ-10 самых высокооплачиваемых вакансий \n"
          f"2. Выйти из программы\n")

    user_choice = int(input("Введите ваш выбор: "))
    if user_choice == 1:
        data = work_with_file()
        top_ten(data)

    if user_choice == 2:
        quit()


if __name__ == "__main__":
    main()

