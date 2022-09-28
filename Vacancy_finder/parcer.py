from classes import *
import random


def main():
    key_word = input("Привет! Введите ключевое слово, по которому необходимо искать вакансии: -> ")
    print("Спасибо! Начинаем искать вакансии на HH.ru и SuperJob")
    v = Vacancy()
    v.parse_vacancy_hh(key_word)


main()