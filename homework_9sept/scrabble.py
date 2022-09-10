import random
num_letters = {"а":8,"б":2,"в":4,"г":2,"д":4,"е":8,"ё":1,"ж":1,"з":2,"и":5,"й":1,"к":4,"л":4,"м":3,"н":5,"о":10,
            "п":4,"р":5,"с":5,"т":5,"у":4,"ф":1,"х":1,"ц":1,"ч":1,"ш":1,"щ":1,"ъ":1,"ы":2,"ь":2,"э":1,"ю":1,"я":2}
letters_list = []
scores_1 = 0
scores_2 = 0

def random_tiles(user_1_name, user_2_name, num_letters, letters_list):
    '''
    раздаёт случайные буквы игрокам и печатает значения этих раздач (принт user_1_tiles user_2_tiles)
    '''
    for letter, num in num_letters.items():
        letters_list.extend(letter * int(num))
    # перемешиваю буквы и беру от них отрезок из 7 штук
    random.shuffle(letters_list)
    user_1_tiles = letters_list[:7]
    user_2_tiles = letters_list[8:15]
    print(f"{user_1_name} - буквы {list(user_1_tiles)}")
    print(f"{user_2_name} - буквы {list(user_2_tiles)}")
    return user_1_tiles, user_2_tiles

def check_word(user_word, user_tiles, turn_counter):
    '''
    проверяет, есть ли у пользователя нужные буквы для слова, которое он ввёл
    '''
    for letter in list(user_word):
        if letter not in user_tiles:
            print(f"У вас нет такой буквы {letter}")
            return False
    return True

def real_word_check(user_word, user_tiles):
    '''
    проверяет, существует ли слово, набранное пользователем с помощью файла русских слов, добавляет букву, если такого слова нет
    '''
    with open("russian_word.txt", "r", encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            if line.rstrip("\n") not in user_word:
                continue
            else:
                return True
        print("Такого слова нет. Игрок не получает баллов.")
        # добавить одну букву игроку
        random.shuffle(letters_list)
        user_tiles.extend(letters_list[0])
        print(f"Добавляю букву {letters_list[0]}")
        return False

def turn(user_name, user_tiles, scores, game, turn_counter):
    '''
    выдаёт актуальный список букв и принимает слово от пользователя
    вызывает функции с проверками
    совершает операции после успешного хода (добавлет баллы, убирает использованные буквы, добавляет новые)

    '''
    while game:
        print(f"{user_name},Ваш ход. Ваш список букв: {user_tiles}")
        user_word = input(f"{user_name}, введите ваше слово: ")
        if user_word == "stop":
            game = False
            break
        else:
            # вызываю функцию, которая проверяет слово, введённое игроком. Если функция возвращает False - просим ввести слово заново
            if check_word(user_word, user_tiles, turn_counter):
                # функция, которая проверяет, есть ли слово в файлике со словами
                if real_word_check(user_word, user_tiles):
                    print("Отличное слово")
                    # добавляем баллы, убираем использованные буквы, добавляем столько же новых
                    scores += len(user_word)
                    print(f"У игрока {user_name} сейчас {scores} б.")
                    random.shuffle(letters_list)
                    user_tiles.extend(letters_list[:len(user_word)])
                    for letter in list(user_word):
                        i = 0
                        if letter in user_tiles:
                            user_tiles.pop(i)
                            i += 1
                    print(f"Добавляю буквы {letters_list[:len(user_word)]}")
                    break
                else:
                    turn_counter += 1
                    break

    return scores, game

if __name__ == "__main__":

    print("Привет, мы начинаем игру в скрэббл.")
    user_1_name = input("Введите имя первого игрока: ")
    user_2_name = input("Введите имя второго игрока: ")
    print(f"{user_1_name} vs {user_2_name}")

    # вызываю функцию, которая раздаёт случайные буквы игрокам и печатает значения этих раздач (принт user_1_tiles user_2_tiles)
    user_1_tiles, user_2_tiles = random_tiles(user_1_name, user_2_name, num_letters, letters_list)

    # меняю ход
    turn_counter = 0
    game = True
    while game:
        if turn_counter % 2 == 0:
            scores_1, game = turn(user_1_name, user_1_tiles, scores_1, game, turn_counter)
        else:
            scores_2, game = turn(user_2_name, user_2_tiles, scores_2, game, turn_counter)
        turn_counter += 1


        # печатаю статистику (Победил(имя) счёт такой-то)
    if scores_1 > scores_2:
        print(f"Победитель {user_1_name}")
        print(f"Счёт {scores_1} : {scores_2}")
    else:
        print(f"Победитель {user_2_name}")
        print(f"Счёт {scores_2} : {scores_1}")
