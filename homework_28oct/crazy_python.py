# Часть 1

def iss(arg1, arg2):
    """
    сравнивает два переданных параметра по ссылке на объект и по значению
    """
    arg1_id = id(arg1)
    arg2_id = id(arg2)

    if arg1_id == arg2_id and arg1 == arg2:
        return f"""Две переменные ссылаются на один и тот же адрес в памяти, имеют одинаковые значения\n
        id первой переменной: {arg1_id}\n
        id второй переменной: {arg2_id}\n
        Значение первой переменной: {arg1}\n
        Значение второй переменной: {arg2}\n
        """

    elif arg1_id != arg2_id and arg1 == arg2:
        return f"""Две переменные ссылаются на разные адреса в памяти, имеют одинаковые значения\n
        id первой переменной: {arg1_id}\n
        id второй переменной: {arg2_id}\n
        Значение первой переменной: {arg1}\n
        Значение второй переменной: {arg2}\n"""

    elif arg1_id == arg2_id and arg1 != arg2:
        return f"""Две переменные ссылаются на один и тот же адрес в памяти, имеют разные значения\n
        id первой переменной: {arg1_id}\n
        id второй переменной: {arg2_id}\n
        Значение первой переменной: {arg1}\n
        Значение второй переменной: {arg2}\n"""

    elif arg1_id != arg2_id and arg1 != arg2:
        return f"""Две переменные ссылаются на разные адреса в памяти, имеют разные значения\n
        id первой переменной: {arg1_id}\n
        id второй переменной: {arg2_id}\n
        Значение первой переменной: {arg1}\n
        Значение второй переменной: {arg2}\n"""


# A = 'spam'
# B = A
# B = 'shrubbery'
# print(iss(A, B))

# A = ['spam']
# B = A
# B[0] = 'shrubbery'
# print(iss(A, B))

# A = ['spam']
# B = A[:]
# B[0] = 'shrubbery'
# print(iss(A, B))

# print(iss([], []))
# print(iss('', ''))
# print(iss({}, {}))

# x = y = [1, True, [1, 2]]
# y[2] = [-1, -2]
# print(iss(x, y))

# x = 5
# y = 5
# print(iss(x, y))

# x, y = [1, [2]], [1, [2]]
# print(iss(x, y))


# Часть 2.1

# class Int(int):
#     """
#     реализация класса Int для сложения чисел и строк с помощью перегрузки операции
#     """
#     def __init__(self, value):
#         super().__init__()
#         self.value = value
#
#     def __add__(self, other):
#         super().__add__(other)
#         if type(other) is str:
#             try:
#
#                 if other == "один":
#                     int_other = 1
#                 elif other == "два":
#                     int_other = 2
#                 elif other == "три":
#                     int_other = 3
#                 elif other == "четыре":
#                     int_other = 4
#                 elif other == "пять":
#                     int_other = 5
#
#                 else:
#                     int_other = int(other)
#
#                 return self.value + int_other
#
#             except ValueError:
#                 return "TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5."
#
#         else:
#             raise TypeError(f"unsupported operand type(s) for +: 'Int' and {type(other)}")
#
#
#
# # x = Int(5)
# # print(x + '5')
# # print(x + 'один')
# # print(x + 'пять')
# # print(x + 'шесть')
# # print(x + 'a')
# # print(x + (1,))


# Часть 2.2

def crazy_python(method):
    """
    декоратор для изменения поведения стандартной функции сложения
    """

    def wrapper(self, other):

        if type(other) is str:
            try:
                if other == "один":
                    int_other = 1
                elif other == "два":
                    int_other = 2
                elif other == "три":
                    int_other = 3
                elif other == "четыре":
                    int_other = 4
                elif other == "пять":
                    int_other = 5
                else:
                    int_other = int(other)

                return method(self, int_other)

            except ValueError:
                return "TypeError: справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5."

        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Int' and {type(other)}")

    return wrapper


class Int(int):
    """
    реализация класса Int для сложения чисел и строк с помощью декоратора
    """

    def __init__(self, value):
        super().__init__()
        self.value = value

    @crazy_python
    def __add__(self, other):
        return super().__add__(other)


x = Int(5)

# print(x + '5')
# print(x + 'один')
# print(x + 'пять')
# print(x + 'шесть')
# print(x + 'a')
# print(x + (1,))