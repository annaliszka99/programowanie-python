from getkey import getkey
from functions import clear_screen


class CardView:
    def __init__(self, card):
        self.card = card
        self.__display_navigation_menu()
        self.__show_card()
        done = False
        while not done:
            done = self.__run_keys_service()

    @staticmethod
    def __display_navigation_menu():
        clear_screen()
        print("[1] Edit question [2] Edit answer [b] Back")

    def __run_keys_service(self):
        key = getkey()
        if key == 'b':
            return True
        elif key == '1':
            print("\nEnter new question:")
            question = input()
            self.card.question = question
        elif key == '2':
            print("\nEnter new answer:")
            answer = input()
            self.card.answer = answer
        self.__display_navigation_menu()
        self.__show_card()

    def __show_card(self):
        print("\nEdit card")
        print("\nq: " + self.card.question)
        print("a: " + self.card.answer)
