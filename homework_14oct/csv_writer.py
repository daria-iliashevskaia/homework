from data_form import get_all_info, list_form, animal_dicts_form, shelter_dicts_form
import csv


def csv_simple_writer(filename: str, name_list: set) -> dict:

    """
    Записывает список в файл сsv файл и возвращает словарь
    """

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        sd = csv.writer(file)
        name_dict = {}
        for i, j in enumerate(list(name_list)):
            sd.writerow([i + 1, j])
            name_dict[j] = str(i + 1)
    return name_dict


def csv_animal_dict_writer(animal_dict_list: list, type_dict: dict, breed_dict: dict, colour_dict: dict):

    """
    Записывает список словарей в csv файл и заменяет значения на индексы внешнего ключа в таблице animal_dict
    """

    csv_columns = ['id_animal', 'animal_id', 'fk_type', 'animal_name', 'fk_breed', 'fk_colour_1', 'fk_colour_2', 'date_of_birth']
    with open('animal_dict.csv', 'w', newline='', encoding='utf-8') as f:
        sd = csv.DictWriter(f, fieldnames=csv_columns)
        sd.writeheader()
        for animal_dict in animal_dict_list:
            animal_dict['fk_type'] = type_dict[animal_dict['fk_type']]
            animal_dict['fk_breed'] = breed_dict[animal_dict['fk_breed']]
            animal_dict['fk_colour_1'] = colour_dict[animal_dict['fk_colour_1']]
            animal_dict['fk_colour_2'] = colour_dict[animal_dict['fk_colour_2']]

            sd.writerow(animal_dict)


def csv_shelter_info_writer(shelter_dict_list: list, outcome_subtype: dict, outcome_type: dict):

    """
    Записывает список словарей в csv файл и заменяет значения на индексы внешнего ключа в таблице animal_dict
    """

    csv_columns = ['index',
                   'fk_animal_id',
                   'fk_outcome_subtype',
                   'fk_outcome_type',
                   'outcome_month',
                   'outcome_year',
                   'age_upon_outcome']

    with open('shelter_info.csv', 'w', newline='', encoding='utf-8') as f:

        sd = csv.DictWriter(f, fieldnames=csv_columns)
        sd.writeheader()
        for info_dict in shelter_dict_list:
            info_dict['fk_outcome_subtype'] = outcome_subtype[info_dict['fk_outcome_subtype']]
            info_dict['fk_outcome_type'] = outcome_type[info_dict['fk_outcome_type']]

            sd.writerow(info_dict)


def main():

    reader = get_all_info()

    # Формирую данные для таблиц по необходимым параметрам
    breed_list = list_form(reader, 5)
    outcome_subtype_list = list_form(reader, 9)
    outcome_type_list = list_form(reader, 10)
    colour_list = list_form(reader, 6).union(list_form(reader, 7))
    type_list = list_form(reader, 3)

    # Формирую словарь с данными для таблицы животных "animals"
    animal_dict_list = animal_dicts_form()

    # Записываю данные по таблицам с породами "breeds", цветами "colours",
    # типами программ "outcome_type", подтипами программ "type_list" в файл csv
    breed_dict = csv_simple_writer('breed_dict.csv', breed_list)
    colour_dict = csv_simple_writer('colour_dict.csv', colour_list)
    type_dict = csv_simple_writer('type_dict.csv', type_list)

    outcome_subtype = csv_simple_writer('outcome_subtype.csv', outcome_subtype_list)
    outcome_type = csv_simple_writer('outcome_type.csv', outcome_type_list)

    # Записываю список словарей с животными "animals" в файл csv,
    # меняя данные с породами, цветами, типами и подтипами программ на соответствующие id
    csv_animal_dict_writer(animal_dict_list, type_dict, breed_dict, colour_dict)

    # Формирую словарь с данными для таблицы инфо о приюте "shelter_info"
    shelter_dict_list = shelter_dicts_form()

    # Записываю список словарей с инфо о приюте "shelter_info" в файл csv,
    # меняя данные с id животного, типом и подтипом программы,
    # мес и годом приёма и возрастом животного на соответствующие id
    csv_shelter_info_writer(shelter_dict_list, outcome_subtype, outcome_type)


if __name__ == '__main__':

    main()