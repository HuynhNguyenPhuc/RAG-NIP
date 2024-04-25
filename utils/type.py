from pydantic import BaseModel

class Sentence(BaseModel):
    def __init__(self, sentence):
        self.sentence = sentence