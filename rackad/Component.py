class Component:
    def __init__(self, number: str, name: str):
        self.number = number
        self.name = name

    def build(self):
        raise NotImplementedError(type(self))
