

def universal_file_hh(file_to_convert) -> list:
    """
    Форматирует передаваемый файл в список название, зарплата, ссылка, описание
    """
    universal_file = {}
    universal_file_list = []

    for el in file_to_convert:
        universal_file["name"] = el["items"][0]["name"]
        universal_file["salary"] = el["items"][0]["salary"]
        universal_file["url"] = el["items"][0]["alternate_url"]
        universal_file["description"] = el["items"][0]["snippet"]

        universal_file_list.append(universal_file)

    return universal_file_list

