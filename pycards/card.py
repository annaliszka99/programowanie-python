from marshmallow_dataclass import dataclass
from marshmallow import Schema, fields, post_load


class Card:
    def __init__(self, question, answer, memorized):
        self.question = question
        self.answer = answer
        self.memorized = memorized


class CardSchema(Schema):
    question = fields.Str()
    answer = fields.Str()
    memorized = fields.Bool()

    @post_load
    def make_card(self, data, **kwargs):
        return Card(**data)


