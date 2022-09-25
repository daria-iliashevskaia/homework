def file_read_():
    """
    Обработка текста
    """
    with open("api.txt") as file:
        content = file.readlines()
    return content


def filter_command(file, text) -> list:
    """
    Фильтрация данных по ключевому слову
    """
    filter_text = filter(lambda line: text in line, file)
    list_filter_text = []
    for item in filter_text:
        list_filter_text.append(" ".join((item.replace("- - ", "").split(" "))[:7]))
    return list_filter_text


def map_command(file, num) -> list:
    """
    Выдача данных в определённом столбце
    """
    map_text = map(lambda element: element.split(" ")[int(num)], file)
    return list(map_text)


def unique_command(file, _) -> list:
    """
    Вывод списка уникальных данных
    """
    unique_text = set(list(file))
    return list(unique_text)


def sorted_command(file, com) -> list:
    """
    Сортировка данных
    """
    x = False
    if "desc" in com:
        x = True
    sorted_text = sorted(file, reverse=x)
    return list(sorted_text)


def limit_command(file, limit) -> list:
    """
    Возвращает количество строк согласно указанным лимитам
    """
    limit_text = (element for element in list(file)[:int(limit)])
    return list(limit_text)



