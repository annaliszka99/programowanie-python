from marshmallow import Schema, fields, post_load
from card import CardSchema


class Set:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards


# pozwala interpretować json
class SetSchema(Schema):
    name = fields.Str()
    cards = fields.List(fields.Nested(CardSchema))

    @post_load
    def make_set(self, data, **kwargs):
        return Set(**data)


class Sets:
    def __init__(self, sets):
        self.sets = sets


class SetsSchema(Schema):
    sets = fields.List(fields.Nested(SetSchema))

    @post_load
    def make_set(self, data, **kwargs):
        return Sets(**data)
