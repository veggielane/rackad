import cadquery as cq
def rack_height(u):
  return 44.45 * u - 0.794



class Component:
    def __init__(self, number:str, name:str):
        self.number = number
        self.name = name

    def build(self):
        raise NotImplementedError(type(self))


class Part(Component):
    def __init__(self,number:str, name:str):
        super(Component, self).__init__(number, name)
