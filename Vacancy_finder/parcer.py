from classes import *
import random


def main():
    key_word = input("Привет! Введите ключевое слово, по которому необходимо искать вакансии: -> ")
    print("Спасибо! Начинаем искать вакансии на HH.ru и SuperJob")
    v = Vacancy()
    print("Ищу на HH...")
    v.parse_vacancy_hh(key_word)
    print("Ищу на SuperJob...")
    v.parse_vacancy_sj(key_word)


    print(f"Список готов!\nВы можете вывести:\n"
          f"1. Топ-10 самых высокооплачиваемых вакансий \n"
          f"2. Вакансии без опыта работы\n"
          f"3. Выйти из программы\n")

    user_choice = int(input("Введите ваш выбор: "))
    if user_choice == 1:
        pass

    if user_choice == 2:
        pass

    if user_choice == 3:
        quit()

main()