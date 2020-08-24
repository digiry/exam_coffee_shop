# pylint: disable=too-few-public-methods
class Customer:
    def order(self, menu_name: str):
        pass


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
