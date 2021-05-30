import time
from functions import clear_screen
from getkey import getkey, keys
from setsview import SetsView
from learnview import LearnView


class MainView:
    def __init__(self):
        self.__display_navigation_menu()
        self.__show_greetings()
        while True:
            self.__run_keys_service()

    @staticmethod
    def __display_navigation_menu():
        clear_screen()
        print("[1] Learn [2] Show and Edit Sets [q] Quit")

    @staticmethod
    def __show_greetings():
        print("\nWelcome to PyCards !!")

    def __process_quit(self):
        print("Press y if you are sure you want to exit")
        if getkey() == 'y':
            print("Thanks for using PyCards")
            quit()
        else:
            print("Cancelled")
            time.sleep(1)
            self.__display_navigation_menu()

    def __run_keys_service(self):
        key = getkey()
        if key == keys.Q:
            self.__process_quit()
        elif key == '1':
            LearnView()
        elif key == '2':
            SetsView()
        self.__display_navigation_menu()
        self.__show_greetings()
