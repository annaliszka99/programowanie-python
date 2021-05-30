import os

from functions import clear_screen
from learncardsview import LearnCardsView
from setsmanager import SetsManager
from getkey import getkey, keys


class LearnView:
    def __init__(self):
        self.sets_manager = SetsManager()
        self.__display_navigation_menu()
        self.sets_manager.show_list_of_sets()
        done = False
        while not done:
            done = self.__run_keys_service()

    def __display_navigation_menu(self):
        clear_screen()
        print("[b] Back")
        if len(self.sets_manager.sets) > 0:
            print("Select set using UP or DOWN arrow and press Enter")
        else:
            print("\nThere is no sets, firstly you must create one")

    def __run_keys_service(self):
        key = getkey()
        if key == 'b':
            return True
        elif key == keys.DOWN:
            self.sets_manager.select_next_set()
        elif key == keys.UP:
            self.sets_manager.select_prev_set()
        elif key == keys.ENTER:
            LearnCardsView(self.sets_manager.sets[self.sets_manager.selected], self.sets_manager.selected)
        self.__display_navigation_menu()
        self.sets_manager.show_list_of_sets()
