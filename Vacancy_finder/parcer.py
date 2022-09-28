from copy import deepcopy
from classes import *


def top_ten(key_word):
    v_hh = HH()
    all_data = v_hh.get_request(key_word)
    temp_data = deepcopy(all_data)
    salary_list = []
    for job in temp_data:
        if job["salary"] is not None:
            salary_list.append(job["salary"]["from"])

    salary_list = list(filter(None, salary_list))

    counter = 1
    for point in sorted(salary_list, reverse=True):
        if counter == 11:
            break
        for data in temp_data:
            try:
                data["salary"]["from"]
            except:
                continue

            if data["salary"]["from"] == point:
                print(f"{counter}. {data['name']}\n")
                print(f"Зарплата от {data['salary']['from']} руб.\n")
                print(f"Условия: {data['snippet']['requirement'] + data['snippet']['responsibility']}\n")
                temp_data.remove(data)
                break
        counter += 1


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
        top_ten(key_word)

    if user_choice == 2:
        quit()

main()
