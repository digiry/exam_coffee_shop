# pylint: disable=too-few-public-methods, no-self-use
from typing import List, Any


class MenuItem:
    def __init__(self, name: str, price: int) -> None:
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    def cost(self) -> int:
        return self._price


class Menu:
    items: List[MenuItem]

    def __init__(self, items: List[MenuItem]) -> None:
        self.items = items

    def choose(self, name: str) -> Any:
        for item in self.items:
            if item.name == name:
                return item
        return None


class Coffee:
    def __init__(self, menu_item: MenuItem) -> None:
        self._name = menu_item.name
        self._price = menu_item.cost()

    def __repr__(self) -> str:
        return f"name:{self._name}, price: {self._price}"


class Barista:
    def make_coffee(self, menu_item: MenuItem) -> Coffee:
        coffee = Coffee(menu_item=menu_item)
        return coffee


class Customer:
    def order(self, menu_name: str, menu: Menu, barista: Barista):
        menu_item = menu.choose(menu_name)
        coffee = barista.make_coffee(menu_item=menu_item)
        print(f"Order menu name: {menu_name}")
        print(f"Made menu - {coffee}")


def main():
    my_shop_menu_items = []
    my_shop_menu_items.append(MenuItem(name="아이스아메리카노", price=3000))
    my_shop_menu_items.append(MenuItem(name="아이스라테", price=3500))
    my_shop_menu_items.append(MenuItem(name="아메리카노", price=2000))
    my_shop_menu_items.append(MenuItem(name="라테", price=2500))

    my_shop_menu = Menu(items=my_shop_menu_items)

    customer1 = Customer()
    barista1 = Barista()

    customer1.order(menu_name="아이스아메리카노", menu=my_shop_menu, barista=barista1)


if __name__ == "__main__":
    main()
