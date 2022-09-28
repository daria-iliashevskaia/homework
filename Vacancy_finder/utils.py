
def universal_file_hh(file_to_convert) -> list:
    """
    Форматирует передаваемый файл в список название, зарплата, ссылка, описание
    """
    universal_file = {}
    universal_file_list = []

    for el in file_to_convert:
        universal_file["name"] = el["name"]
        if el["salary"] is None:
            universal_file["salary"] = "не указана"
        else:
            universal_file["salary"] = "от " + str(el["salary"]["from"])
        universal_file["url"] = el["alternate_url"]
        universal_file["description"] = str(el["snippet"]["requirement"]) + str(el["snippet"]["responsibility"])
        universal_file_list.append(universal_file.copy())

    return universal_file_list

