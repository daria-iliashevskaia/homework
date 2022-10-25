
lst = [1, 2, None, None]


def insert(massiv, index, value):
    """
    вставляет элемент по индексу
    """
    i = 0

    for el in massiv:
        if el is None:
            massiv[i] = massiv[i-1]
            massiv[index] = value
            break
        else:
            i += 1

    return massiv


def read(massiv, index):
    """
    читает элемент массива
    """
    return massiv[index]


def write(massiv, element):
    """
    записывает элемент массива в конец
    """
    i = 0
    for el in massiv:
        if el is None:
            massiv[i] = element
        else:
            i += 1
            continue

    return massiv


def delete(massiv, element):
    """
    удаляет элемент по индексу
    """
    i = element
    for el in massiv:
        massiv[i] = massiv[i+1]
        i += 1
        if el is None:
            break
    return massiv

# читаем
# print(read(lst, 2))
# записываем в конец
# print(write(lst, 4))
# вставляем по индексу
# print(insert(lst, 1, 3))
# удаляем по индексу
# print(delete(lst, 0))
