
class Storage:
    def __init__(self, item: dict, capacity: int) -> None:
        self._item = item
        self._capacity = capacity

    @property
    def item(self) -> dict:
        return self._item

    @property
    def capacity(self) -> int:
        return self._capacity - sum(self.item.values())

    def add(self, product: str, amount: int) -> None:
        """
        увеличивает запас items
        """
        if product in self.item.keys():
            self.item[product] += amount
        else:
            self.item[product] = amount

    def remove(self, product: str, amount: int) -> bool:
        """
        уменьшает запас items
        """
        if amount < self.item[product]:
            self.item[product] -= amount
            return True
        else:
            return False

    @property
    def get_unique_items_count(self) -> int:
        """
        возвращает количество уникальных товаров
        """
        return len(self.item)


class Store(Storage):
    """
    класс "Склад". В нем хранится любое количество любых товаров.
    Store не может быть заполнен если свободное место закончилось
    """
    def __init__(self, item: dict, capacity: int = 100) -> None:  # по умолчанию вместительность склада = 100
        super().__init__(item, capacity)

    def add(self, product: str, amount: int) -> bool:
        """
        увеличивает запас items, если число переданных товаров меньше вместительности склада
        """
        if amount < self.capacity:
            super().add(product, amount)
            return True
        else:
            return False


class Shop(Storage):
    """
    класс "Магазин".
    В нем хранится любое количество любых товаров.
    Shop не может быть заполнен если свободное место закончилось и не может хранить больше 5 товаров
    """

    def __init__(self, item: dict, capacity: int = 20) -> None:  # по умолчанию вместительность магазина = 100
        super().__init__(item, capacity)

    def add(self, product: str, amount: int) -> bool:
        if amount < self.capacity:
            if self.get_unique_items_count < 5:
                super().add(product, amount)
                return True
        else:
            return False


class Request:
    def __init__(self, from_: str, to: str, amount: int, product: str) -> None:
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.product = product

    def __repr__(self) -> str:
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"
