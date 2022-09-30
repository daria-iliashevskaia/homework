import re

import requests
from bs4 import BeautifulSoup as BS
from abc import ABC, abstractmethod


class Engine(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def get_request(self, *args):
        pass


class HH(Engine):

    def get_request(self, key_word: str):
        """
        Возвращает список с данными о вакансии с HH
        """
        job_list = []
        for i in range(50):    # количество страниц
            url = 'https://api.hh.ru/vacancies'
            par = {"text": key_word, 'area': '113', 'per_page': '10', 'page': i}
            response = requests.get(url, params=par)
            response_json = response.json()["items"]
            job_list.extend(response_json)

        universal_file = {}
        job_list_hh = []

        for el in job_list:
            universal_file["name"] = el["name"]
            if el["salary"] is None:
                universal_file["salary"] = "не указана"
            else:
                universal_file["salary"] = str(el["salary"]["from"])
            universal_file["url"] = el["alternate_url"]
            universal_file["description"] = str(el["snippet"]["requirement"]) + str(el["snippet"]["responsibility"])
            job_list_hh.append(universal_file.copy())

        return job_list_hh


class Superjob(Engine):

    def get_request(self, key_word: str) -> list:
        """
        Возвращает список с данными о вакансии с SJ
        """
        list_of_names = []
        list_of_descriptions = []
        list_of_salaries = []
        for i in range(3):
            num_page = i + 1
            url = f"https://russia.superjob.ru/vacancy/search/?keywords={key_word}&page={num_page}"
            response = requests.get(url)
            soup = BS(response.text, "lxml")

            names = soup.find_all("span", class_="_9fIP1 _249GZ _1jb_5 QLdOc")
            list_of_names += names
            descriptions = soup.find_all('div', class_='_2d_Of _2J-3z _3B5DQ')
            list_of_descriptions += descriptions
            salaries = soup.find_all("span", class_="_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi")
            list_of_salaries += salaries

        job_list_sj = []

        for i in range(len(list_of_names)):
            sal = list_of_salaries[i].text.replace("\xa0", "")
            # sal_clear = re.findall(r'(^\d{4,6})|[а-я]{2}(\d{4,6})', sal)
            sal_clear = re.findall(r'\d{4,6}', sal)
            dict = {
                    "name": list_of_names[i].text,
                    "salary": sal_clear,
                    "url": "https://russia.superjob.ru/" + list_of_names[i].a["href"],
                    "description": list_of_descriptions[i].text
                    }
            job_list_sj.append(dict.copy())

        return job_list_sj


class Vacancy:

    def __init__(self):
        self.url = None
        self.title = None
        self.salary = None
        self.description = None

    def __repr__(self) -> str:
        return f"{self.title}|{self.url}|{self.salary}|{self.description}\n"

    def parse_vacancy_hh(self, key_word: str):
        """
        Записывает значения полей объекта класса Vacancy в соответствии с найденной вакансией,
        меняет переменные полей согласно списку,
        создаёт объект на каждую вакансию,
        записывает этот объект в файл с помощью __repr__
        """
        hh_vacances = HH()
        universal_file_list = hh_vacances.get_request(key_word)

        file_vacances_list_hh = []
        # создаю список со строковыми значениями объектов вакансий
        for job in universal_file_list:
            self.title = job["name"]
            self.url = job["url"]
            self.salary = job["salary"]
            self.description = job["description"]
            file_vacances_list_hh.append(str(self))

            with open("vacances.txt", "w", encoding="utf-8") as file:
                # записываю значения объектов вакансий с hh в файл
                for vacancy in file_vacances_list_hh:
                    file.write(vacancy)

        return file_vacances_list_hh

    def parse_vacancy_sj(self, key_word: str) -> list:
        """
        Записывает значения полей объекта класса Vacancy в соответствии с найденной вакансией,
        меняет переменные полей согласно списку,
        создаёт объект на каждую вакансию,
        записывает этот объект в файл с помощью __repr__
        """
        sj_vacances = Superjob()
        universal_file_list = sj_vacances.get_request(key_word)
        # создаю объект класса SuperJob, чтобы создать список с данными формата
        # {name: , "salary": , "url": , "description": }
        file_vacances_list_sj = []
        # создаю список с вакансиями в виде строк, чтобы его записать в текстовый

        for job in universal_file_list:
            self.title = job["name"]
            self.url = job["url"]
            self.salary = job["salary"]
            self.description = job["description"]
            file_vacances_list_sj.append(str(self))

            with open("vacances.txt", "a", encoding="utf-8") as file:
                # записываю значения объектов вакансий с SJ в файл
                for vacancy in file_vacances_list_sj:
                    file.write(vacancy)

        return file_vacances_list_sj

