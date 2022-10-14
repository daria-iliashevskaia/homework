import requests
import csv


def get_all_info() -> list:

    """
    Возвращает список с данными из файла csv
    """

    response = requests.get("https://raw.githubusercontent.com/skypro-008/SQL_ISA/main/main_animals.csv")
    with open('main_animals.csv', 'w', encoding='utf-8') as file:
        file.write(response.text)

    with open("main_animals.csv", "r", encoding='utf-8') as f:
        reader = list(csv.reader(f))

    return reader


def list_form(reader: list, text_index: int) -> set:

    """
    Формирует уникальный список выбранных значений (по индексу)
    """

    name_list = []
    for i in reader:
        name_list.append(i[text_index])

    unique_list = set(name_list[1:])
    return unique_list


def animal_dicts_form() -> list:

    """
    Формирует словарь с нужными данными для таблицы "animals"
    """

    animals_dict = {}
    animal_list = []
    new_animal_list = []

    with open("main_animals.csv", "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            animal_list.append(row)

    for animal in animal_list:

        animals_dict['animal_id'] = animal['animal_id']
        animals_dict['fk_type'] = animal['animal_type']
        animals_dict['animal_name'] = animal['name']
        animals_dict['fk_breed'] = animal['breed']
        animals_dict['fk_colour_1'] = animal['color1']
        animals_dict['fk_colour_2'] = animal['color2']
        animals_dict['date_of_birth'] = animal['date_of_birth']

        new_animal_list.append(animals_dict.copy())

    return new_animal_list


def shelter_dicts_form() -> list:

    """
    Формирует словарь с нужными данными для таблицы "shelter_info"
    """

    shelter_dict = {}
    shelter_list = []
    new_shelter_list = []

    with open("main_animals.csv", "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            shelter_list.append(row)

    for animal in shelter_list:

        shelter_dict['index'] = animal['index']
        shelter_dict['fk_animal_id'] = animal['animal_id']
        shelter_dict['fk_outcome_subtype'] = animal['outcome_subtype']
        shelter_dict['fk_outcome_type'] = animal['outcome_type']
        shelter_dict['outcome_month'] = animal['outcome_month']
        shelter_dict['outcome_year'] = animal['outcome_year']
        shelter_dict['age_upon_outcome'] = animal['age_upon_outcome']

        new_shelter_list.append(shelter_dict.copy())

    return new_shelter_list





