import csv
import pandas as pd


def select_sorted(sort_columns, filename, limit=10):
    """
    Функция сортирует массив по указанным колонкам, и выписывает определённое количество строк в отдельный файл csv
    :param sort_columns:
    :param filename:
    :param limit:
    """
    df = pd.read_csv('all_stocks_5yr.csv')
    sorted_df = df.sort_values(by=sort_columns, ascending=False)
    res = sorted_df.head(limit)
    res.to_csv(filename)


# select_sorted(sort_columns=["high"], limit=10, filename='sorted.csv')


def get_data(date, name, filename):
    """
    Функция фильтрует массив по входным данным (дата, имя) и записывает итог в указанный файл
    :param date:
    :param name:
    :param filename:
    """
    with open('all_stocks_5yr.csv') as f:
        reader = csv.reader(f)
        next(reader)

        with open(filename, 'w') as f1:
            writer = csv.writer(f1)
            writer.writerow(['date', 'open', 'high', 'low', 'close', 'volume', 'name'])

            for row in reader:
                if row[0] == date and row[6] == name:
                    writer.writerow(row)


# get_data(date = "2013-12-05", name="AIZ", filename="filtered.csv")

