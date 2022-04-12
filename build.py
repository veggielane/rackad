from rackad.lib import RackSize
import rackad.panels as panels
import rackad.mount as mount
import cadquery as cq
from rackad.builder import build


parts = [
    panels.Blank(RackSize.NINETEEN, 1),
    panels.Blank(RackSize.NINETEEN, 2),
    panels.Blank(RackSize.TEN, 1),
    panels.Blank(RackSize.TEN, 2),
    mount.Switch8(),
]

build = build(parts)
