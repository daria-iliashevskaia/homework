import json


def load_questions() -> list:
    """
    Загружает словарь с вопросами из файла
    :return: questions
    """
    with open("questions.json") as file:
        questions = json.load(file)
        return questions


load_questions()