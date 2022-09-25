from util import *


def main():
    """
    Приём команды от пользователя и её обработка
    """
    file = file_read_()

    command_dict = {
        "filter": filter_command,
        "limit": limit_command,
        "map": map_command,
        "sort": sorted_command,
        "unique": unique_command
        }

    user_input = input("Введите команду: ")
    command_list = user_input.split(" | ")

    for i in command_list:
        command, value = i.split()
        if command in command_dict:
            file = command_dict[command](file, value)
        else:
            print("Не могу выполнить данную команду. Повторите ввод.")
    for text in file:
        print(text)


if __name__ == "__main__":
    main()


