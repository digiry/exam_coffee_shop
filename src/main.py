# pylint: disable=too-few-public-methods, no-self-use
from typing import List


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

    def choose(self, name: str) -> MenuItem:
        for item in self.items:
            if item.name == name:
                return item
        return None


class Coffee:
    def __init__(self, menu_item: MenuItem) -> None:
        self._name = menu_item.name
        self._price = menu_item.cost()


class Barista:
    def make_coffee(self, menu_item: MenuItem) -> Coffee:
        coffee = Coffee(menu_item=menu_item)
        return coffee


class Customer:
    def order(self, menu_name: str, menu: Menu, barista: Barista):
        menu_item = menu.choose(menu_name)
        coffee = barista.make_coffee(menu_item=menu_item)
        print(coffee)
