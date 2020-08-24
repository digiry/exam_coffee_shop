# pylint: disable=too-few-public-methods, no-self-use
from typing import List


class MenuItem:
    def __init__(self) -> None:
        self._name = ""

    @property
    def name(self) -> str:
        return self._name


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
        pass


class Barista:
    def make_coffee(self, menu_item: MenuItem) -> Coffee:
        return None


class Customer:
    def order(self, menu_name: str, menu: Menu, barista: Barista):
        menu_item = menu.choose(menu_name)
        coffee = barista.make_coffee(menu_item=menu_item)
        print(coffee)
