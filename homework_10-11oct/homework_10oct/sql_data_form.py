import csv


with open("ads.csv", "r", encoding='utf-8') as file:
    reader = list(csv.reader(file))

authors_list = []
address_list = []

for i in reader:
    authors_list.append(i[2])
    address_list.append(i[5])

unique_authors_list = set(authors_list[1:])
unique_address_list = set(address_list[1:])

with open('authors.csv', 'w', newline='', encoding='utf-8') as file:
    sd = csv.writer(file)
    author_dict = {}
    for i, j in enumerate(list(unique_authors_list)):
        sd.writerow([i + 1, j])
        author_dict[j] = str(i + 1)

with open('address.csv', 'w', newline='', encoding='utf-8') as f:
    sd = csv.writer(f)
    address_dict = {}
    for i, j in enumerate(list(unique_address_list)):
        sd.writerow([i + 1, j])
        address_dict[j] = str(i + 1)

with open('all_ads.csv', 'w', newline='', encoding='utf-8') as f:
    sd = csv.writer(f)
    for i in reader[1:]:
        i[2] = author_dict[i[2]]
        i[5] = address_dict[i[5]]
        sd.writerow(i)

