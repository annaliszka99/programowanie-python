import time
from functions import clear_screen
from getkey import getkey, keys
from setsmanager import SetsManager
from setview import SetView


class SetsView:
    def __init__(self):
        self.sets_manager = SetsManager()
        self.__display_navigation_menu()
        self.sets_manager.show_list_of_sets()
        done = False
        while not done:
            done = self.__run_keys_service()

    def __display_navigation_menu(self):
        clear_screen()
        if len(self.sets_manager.sets) > 0:
            print("[1] New set [2] Edit [3] Delete [b] Back")
        else:
            print("[1] New set [b] Back")

    def __run_keys_service(self):
        key = getkey()
        if key == 'b':
            return True
        elif key == '1':
            SetView(None)
            self.sets_manager.reload_sets()
        elif key == '2' and len(self.sets_manager.sets) > 0:
            SetView(self.sets_manager.sets[self.sets_manager.selected])
            print("Do you want to save changes? (y/other)")
            key = getkey()
            if key == 'y':
                self.sets_manager.save_changes()
            self.sets_manager.reload_sets()
        elif key == '3' and len(self.sets_manager.sets) > 0:
            print("\nAre you sure, you want to remove set named \"" +
                  self.sets_manager.sets[self.sets_manager.selected].name + "\"? (y/other)")
            key = getkey()
            if key == 'y':
                self.sets_manager.remove_selected_set()
            else:
                print("Cancelled")
                time.sleep(1)
        elif key == keys.DOWN and len(self.sets_manager.sets) > 0:
            self.sets_manager.select_next_set()
        elif key == keys.UP and len(self.sets_manager.sets) > 0:
            self.sets_manager.select_prev_set()
        self.__display_navigation_menu()
        self.sets_manager.show_list_of_sets()
