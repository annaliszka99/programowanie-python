import time
from functions import clear_screen
from getkey import getkey, keys
from card import Card
from cardview import CardView


class CardsView:
    def __init__(self, cards):
        self.cards = cards
        self.current_card = 0
        self.__display_navigation_menu()
        self.__show_card()
        done = False
        while not done:
            done = self.__run_keys_service()

    def __display_navigation_menu(self):
        clear_screen()
        if len(self.cards) > 0:
            print("[1] New card [2] Edit [3] Delete [b] Back")
        else:
            print("[1] New card [b] Back")

    def __run_keys_service(self):
        key = getkey()
        if key == 'b':
            return True
        elif key == '1':
            clear_screen()
            print("Creating new card")
            print("\nEnter question and press Enter:")
            question = input()
            print("\nEnter answer and press Enter")
            answer = input()
            self.cards.append(Card(question, answer, False))
            self.current_card = len(self.cards) - 1
            print("\nCard added!")
            time.sleep(1)
        elif key == '2' and len(self.cards) > 0:
            CardView(self.cards[self.current_card])
        elif key == '3' and len(self.cards) > 0:
            self.__remove_card()
        elif key == keys.RIGHT and len(self.cards) > 0:
            if self.current_card < len(self.cards) - 1:
                self.current_card += 1
        elif key == keys.LEFT and len(self.cards) > 0:
            if self.current_card > 0:
                self.current_card -= 1
        self.__display_navigation_menu()
        self.__show_card()

    def __remove_card(self):
        print("\nAre you sure, you want to remove card? (y/n)")
        ok = False
        while not ok:
            key = getkey()
            if key == 'y':
                self.cards.pop(self.current_card)
                ok = True
            elif key == 'n':
                print("Cancelled")
                time.sleep(1)
                ok = True

    def __show_card(self):
        if len(self.cards) > 0:
            print("\nCurrent " + str(self.current_card + 1) + " / " + str(len(self.cards)))
            print("\nq: " + self.cards[self.current_card].question)
            print("a: " + self.cards[self.current_card].answer)
