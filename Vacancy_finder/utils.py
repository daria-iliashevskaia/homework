from operator import itemgetter


def work_with_file():
    """
    Выгружает данные файла vacances.txt
    """
    with open("vacances.txt", "r", encoding='utf-8') as file:
        data = file.read().split("\n")
    return data


def top_ten(some_data):
    """
    Выводит топ 10 вакансий по зарплате
    """
    dt_list = []
    for dt in some_data:
        dt_to_list = dt.split("|")
        try:
            dt_to_list[2] = int(dt_to_list[2])
        except:
            continue
        dt_list.append(dt_to_list)

    dt_sorted = sorted(dt_list, key=itemgetter(2), reverse=True)
    for i in range(10):
        for item in dt_sorted[i]:
            print(item)
        print("="*100)



