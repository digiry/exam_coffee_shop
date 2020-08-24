# pylint: disable=too-few-public-methods, no-self-use
class MenuItem:
    pass


class Menu:
    def choose(self, name: str) -> MenuItem:
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
