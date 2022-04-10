import rackad.panels as panels
import cadquery as cq

part = panels.Blank(1)
build = part.build().val()


build.exportStep(f"outputs/{part.number}.step")
cq.exporters.export(build, f"outputs/{part.number}.stl")