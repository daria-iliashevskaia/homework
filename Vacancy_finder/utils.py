

def universal_file_hh(file_to_convert) -> list:
    """
    Форматирует передаваемый файл в список название, зарплата, ссылка, описание
    """
    universal_file = {}
    universal_file_list = []
    for el in file_to_convert:
        universal_file["name"] = el["name"]
        universal_file["salary"] = el["salary"]
        universal_file["url"] = el["alternate_url"]
        universal_file["description"] = el["snippet"]
        universal_file_list.append(universal_file.copy())

    return universal_file_list

