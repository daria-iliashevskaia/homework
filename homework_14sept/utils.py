import json
from typing import Union
import re


def load_students() -> list:
    """
    Загружает список студентов из файла
    :return: students
    """
    with open("students.json") as file:
        students = json.load(file)
        return students


def load_professions() -> list:
    """
    Загружает список профессий из файла
    :return: professions
    """
    with open("professions.json") as file:
        professions = json.load(file)
        return professions


def get_student_by_pk(pk: Union[int, str], students: list) -> dict:
    """
    Получает словарь с данными студента по его pk
    :param pk:
    :param students:
    :return: student_data
    """
    for student in students:
        if student["pk"] == int(pk):
            student_data = {"full_name": student["full_name"], "skills": student["skills"]}
            print(f"Студент {student['full_name']}")
            student_skills_str = ", ".join(student['skills'])
            print(f"Знает {student_skills_str}")
            return student_data

    print("Такого студента нет")
    quit()


def get_profession_by_title(title: str, professions: list) -> dict:
    """
    Получает словарь с инфо о профе по названию
    :param title:
    :param professions:
    :return:
    """
    for prof in professions:
        if prof["title"] == title:
            prof_data = {"skills": prof["skills"]}
            return prof_data
    print("Нет такой специальности")
    quit()


def login_check(students: list) -> list:
    """
    Проверяет корректность ввода логина
    :param students:
    :return:
    """
    result_list = []
    for student in students:
        login_string = student['login']
        result = re.fullmatch('^[^A-Z](?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,10}[^@$!%*?&_-]$', login_string)
        result_list.append(result)
    return result_list
