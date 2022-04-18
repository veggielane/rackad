from rackad.lib import RackSize
import rackad.panels as panel
import rackad.mount as mount
import cadquery as cq
from rackad.builder import build


parts = [
    panel.FLAT_1U19,
    panel.FLAT_2U19,
    panel.FLAT_1U10,
    panel.FLAT_2U10,
    mount.Switch8(),
]

build = build(parts)
