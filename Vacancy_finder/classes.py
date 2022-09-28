from utils import *
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

    def get_request(self, key_word: str) -> list:
        """
        Возвращает список с данными о вакансии с HH
        """
        job_list = []
        for i in range(70):    # количество страниц
            url = 'https://api.hh.ru/vacancies'
            par = {"text": key_word, 'area': '113', 'per_page': '10', 'page': i}
            response = requests.get(url, params=par)
            response_json = response.json()["items"]
            job_list.extend(response_json)
        return job_list


class Superjob(Engine):

    def get_request(self, key_word: str) -> list:
        """
        Возвращает список с данными о вакансии с HH
        """
        key_word = "python"
        num_page = 2
        url = f"https://russia.superjob.ru/vacancy/search/?keywords={key_word}&page={num_page}"
        response = requests.get(url)
        soup = BS(response.text, "lxml")
        # job_list_superjob = soup.findAll("div", class_="f-test-search-result-item")
        # print(job_list_superjob[0])

        name = soup.find_all("span", class_="_9fIP1 _249GZ _1jb_5 QLdOc")
        description = soup.find_all("span", class_="_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky")
        salary = soup.find_all("span", class_="_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi")

        # print(name)
        # print(description)
        # print(salary)


class Vacancy:

    def __init__(self):
        self.url = None
        self.title = None
        self.salary = None
        self.description = None

    def __repr__(self) -> str:
        return f"Название вакансии: {self.title}\n" \
               f"Ссылка на вакансию: {self.url}\n" \
               f"Зарплата: {self.salary}\n" \
               f"Описание: {self.description}\n" \
               f"_________________________________\n"

    def parse_vacancy_hh(self, key_word: str):
        """
        Записывает значения полей объекта класса Vacancy в соответствии с найденной вакансией,
        меняет переменные полей согласно списку,
        создаёт объект на каждую вакансию,
        записывает этот объект в файл с помощью __repr__
        """
        hh_vacances = HH()
        job_list = hh_vacances.get_request(key_word)
        universal_file_list = universal_file_hh(job_list)

        file_vacances_list = []
        # создаю список со строковыми значениями объектов вакансий
        for job in universal_file_list:
            self.title = job["name"]
            self.url = job["url"]
            self.salary = job["salary"]
            self.description = job["description"]
            file_vacances_list.append(str(self))

            with open("vacances.txt", "w", encoding="utf-8") as file:
                # записываю значения объектов вакансий с hh в файл
                for vacancy in file_vacances_list:
                    file.write(vacancy)


# s = Superjob()
# s.get_request()

