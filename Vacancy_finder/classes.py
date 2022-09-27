from utils import *
import requests
from bs4 import BeautifulSoup as BS
from abc import ABC, abstractmethod
import json


class Engine(ABC):
    """
    Абстрактный класс
    """
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):

    def get_request(self) -> list:
        """
        Возвращает список с данными о вакансии с HH
        """
        job_list = []
        for i in range(70):    # количество страниц
            url = 'https://api.hh.ru/vacancies'
            par = {"text": "python", 'area': '113', 'per_page': '10', 'page': i}
            response = requests.get(url, params=par)
            response_json = response.json()
            job_list.append(response_json)
        return job_list


class Superjob(Engine):

    def get_request(self) -> list:
        """
        Возвращает список с данными о вакансии с HH
        """
        # считывает данные только со второй страницы, нужно дописать цикл
        num_page = 2
        url = f"https://russia.superjob.ru/vacancy/search/?keywords=python&page={num_page}"
        response = requests.get(url)
        soup = BS(response.text, "lxml")
        job_list_superjob = soup.findAll("div", class_="f-test-search-result-item")
        return job_list_superjob


class Vacancy:

    def __init__(self):
        self.url = None
        self.title = None
        self.salary = None
        self.description = None

    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)

    def parse_vacancy_hh(self):
        """
        Записывает значения полей объекта класса Vacancy в соответствии с найденной вакансией
        Нужно: менять переменные полей согласно списку, создавать объект на каждую вакансию, записывать этот объект в файл с помощью repr
        """
        hh_vacances = HH()
        job_list = hh_vacances.get_request()
        universal_file_list = universal_file_hh(job_list) # пофиксить метод universal_file_hh (выдаёт список из одинаковых значений)

        for job in universal_file_list:
            self.title = job["name"]
            self.url = job["url"]
            self.salary = job["salary"]
            self.description = job["description"]

            print(v)



v = Vacancy()
v.parse_vacancy_hh()


# s = Superjob()
# s.get_request()



