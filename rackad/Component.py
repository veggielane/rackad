from numpy import uint


class Component:
    def __init__(self, number: str, name: str, revision:uint = 1):
        self.number = number
        self.name = name
        self.revision = revision

    def build(self):
        raise NotImplementedError(type(self))
