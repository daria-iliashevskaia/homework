from utils import *


def main() -> None:
    item_store = {"печеньки": 5,
                  "собачки": 5,
                  "коробки": 5}

    item_shop = {"печеньки": 1}

    store = Store(item_store)
    shop = Shop(item_shop)

    while True:

        user_from = input("Откуда доставлять? ")
        if user_from == "stop":
            break
        user_to = input("Куда доставлять? ")
        user_product = input("Что доставлять? ")
        user_amount = int(input("Сколько? "))

        user = Request(user_from, user_to, user_amount, user_product)
        print(user)
        if store.remove(user.product, user.amount) and shop.add(user.product, user.amount):
            print('Нужное количество есть на складе')
            print('На складе хранится:\n')
            for name_prod, count in store.item.items():
                print(name_prod, count)

            print('В магазине хранится:\n')

            for name_prod, count in shop.item.items():
                print(name_prod, count)

        elif user.amount > shop.capacity:
            print('В магазин недостаточно места, попробуйте что то другое')
            continue
        else:
            print('Не хватает на складе, попробуйте заказать меньше')
            continue


if __name__ == "__main__":
    main()


