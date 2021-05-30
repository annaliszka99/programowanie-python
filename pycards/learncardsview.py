import random
from functions import clear_screen
from getkey import getkey
from setsmanager import SetsManager


class LearnCardsView:
    def __init__(self, set_item, set_index):
        self.progress = 0
        self.set_item = set_item
        self.set_index = set_index
        self.__setup_learning()
        self.cards = self.set_item.cards
        self.current_card = 0
        self.__count_progress()
        self.__display_navigation_menu()
        self.__show_progress()
        self.__show_card()
        done = False
        while not done:
            done = self.__run_keys_service()

    def __setup_learning(self):
        print("Setup learning of set \"" + self.set_item.name + "\"")
        print("Do you want to continue [c] or learn again [a]?")
        ok = False
        while not ok:
            key = getkey()
            if key == 'c':
                ok = True
            elif key == 'a':
                setsmanager = SetsManager()
                self.set_item = setsmanager.reset_set(self.set_index)
                ok = True

    def __display_navigation_menu(self):
        clear_screen()
        if self.progress == 100:
            print("[b] Back")
        else:
            print("[s] Show answer [b] Back")

    def __run_keys_service(self):
        key = getkey()
        if key == 'b':
            return True
        if key == 's' and self.progress < 100:
            self.__show_answer()
        self.__count_progress()
        self.__display_navigation_menu()
        self.__show_progress()
        self.__show_card()

    def __draw_random_card(self):
        if len(self.cards) > 0:
            self.current_card = random.randint(0, len(self.cards) - 1)
            while self.cards[self.current_card].memorized is True:
                self.current_card = random.randint(0, len(self.cards) - 1)

    def __count_progress(self):
        if len(self.cards) > 0:
            self.progress = (len([card for card in self.cards if card.memorized is True]) / len(self.cards)) * 100
        else:
            self.progress = 100

    def __show_progress(self):
        if len(self.cards) > 0:
            print("\nProgress: " + str(self.progress) + "%")

    def __show_card(self):
        if self.progress < 100:
            self.__draw_random_card()
            print("\nq: " + self.cards[self.current_card].question)
        else:
            if len(self.cards) > 0:
                print("\nYou have nothing to learn in this set")
            else:
                print("\nThis set has no cards !!")

    def __show_answer(self):
        print("a: " + self.cards[self.current_card].answer)
        print("\nDid you guess answer correctly? (y/n)")
        ok = False
        while not ok:
            key = getkey()
            if key == 'y':
                self.cards[self.current_card].memorized = True
                sets_manager = SetsManager()
                sets_manager.update_cards(self.cards, self.set_index)
                ok = True
            elif key == 'n':
                ok = True
