from rackad.Component import Component


class Part(Component):
    def __init__(self, number: str, name: str):
        super(Component, self).__init__(number, name)
