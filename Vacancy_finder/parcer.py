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

main()