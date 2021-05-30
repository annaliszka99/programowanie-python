import codecs
import json
import time
from typing import List
from set import Set, SetsSchema, Sets
import jsonlines


class SetsManager:
    def __init__(self):
        self.json_path = "cards.json"
        self.selected = 0
        self.sets: List[Set] = []
        self.__load_sets()

    def __load_sets(self):
        self.sets.clear()
        file = codecs.open(self.json_path, 'r', 'utf-8')
        sets_json = json.loads(file.read())
        schema = SetsSchema()
        self.sets = schema.load(sets_json).sets

    def show_list_of_sets(self):
        print("\n")
        for index in range(len(self.sets)):
            if index == self.selected:
                print("\033[4m" + self.sets[index].name + "\033[0m")
            else:
                print(self.sets[index].name)

    def select_next_set(self):
        if self.selected < len(self.sets) - 1:
            self.selected += 1

    def select_prev_set(self):
        if self.selected > 0:
            self.selected -= 1

    def reload_sets(self):
        self.__load_sets()

    def remove_selected_set(self):
        self.sets.pop(self.selected)
        schema = SetsSchema()
        sets = Sets(self.sets)
        with jsonlines.open(self.json_path, mode='w') as writer:
            writer.write(schema.dump(sets))
        self.reload_sets()

    def save_changes(self):
        schema = SetsSchema()
        sets = Sets(self.sets)
        with jsonlines.open(self.json_path, mode='w') as writer:
            writer.write(schema.dump(sets))

    def reset_set(self, index):
        for card in self.sets[index].cards:
            card.memorized = False
        schema = SetsSchema()
        sets = Sets(self.sets)
        with jsonlines.open(self.json_path, mode='w') as writer:
            writer.write(schema.dump(sets))
        return self.sets[index]

    def update_cards(self, cards, set_index):
        self.sets[set_index].cards = cards
        schema = SetsSchema()
        sets = Sets(self.sets)
        with jsonlines.open(self.json_path, mode='w') as writer:
            writer.write(schema.dump(sets))


def add_set(name):
    print("Adding " + name)
    sets_manager = SetsManager()
    sets_manager.sets.append(Set(name, []))
    schema = SetsSchema()
    sets = Sets(sets_manager.sets)
    with jsonlines.open(sets_manager.json_path, mode='w') as writer:
        writer.write(schema.dump(sets))
    print("Success")
    time.sleep(1)
