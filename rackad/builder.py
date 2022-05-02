from typing import List
from rackad.Component import Component
import cadquery as cq
import rackad.sheet


def build(components: List[Component]):
    for comp in components:
        print(f"building {comp.name}")
        built = comp.build().val()
        built.exportStep(f"outputs/{comp.number}.step")
        cq.exporters.export(built, f"outputs/{comp.number}.stl")

def show(components: List[Component]):
    return map(lambda comp: comp.build().val(), components)