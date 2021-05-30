import os

from functions import clear_screen
from setsmanager import add_set
from getkey import getkey
from cardsview import CardsView

class SetView:
    def __init__(self, set_item):
        self.set_item = set_item
        if self.set_item is None:
            clear_screen()
            self.__create_new_set()
        else:
            self.__display_navigation_menu()
            done = False
            while not done:
                done = self.__run_keys_service()

    def __display_navigation_menu(self):
        clear_screen()
        print("[1] Rename [2] Edit cards [b] Back")
        print("Set \"" + self.set_item.name + "\" editor")

    def __run_keys_service(self):
        key = getkey()
        if key == 'b':
            return True
        elif key == '1':
            print("\nEnter new name and press Enter:")
            name = input()
            self.set_item.name = name
        elif key == '2':
            CardsView(self.set_item.cards)
        self.__display_navigation_menu()
        return False

    @staticmethod
    def __create_new_set():
        print("Create new set!")
        print("\n")
        print("Type set name and press Enter:")
        ok = False
        while not ok:
            name = input()
            if name.replace(" ", "") == "":
                print("Name can't be empty, type name again and press Enter:")
            else:
                add_set(name)
                ok = True
