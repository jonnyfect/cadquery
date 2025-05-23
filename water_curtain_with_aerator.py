import math
import cadquery as cq

# === CONFIGURATION ===
module_length = 304.8 # 12 inches in mm
outer_diameter = 30.0
wall_thickness = 3.25
inner_diameter = outer_diameter - 2 * wall_thickness
slit_width = 0.5
port_diameter = 6.35 # 1/4" OD tubing
port_depth = 10
aerator_thickness = 5 # Height of the honeycomb structure
hex_size = 5 # Flat-to-flat size of each hex cell

# === MAIN BODY ===
tube = (
    cq.Workplane("XY")
    .circle(outer_diameter / 2)
    .circle(inner_diameter / 2)
    .extrude(module_length)
)

# === CURTAIN SLIT ===
slit = (
    cq.Workplane("XZ")
    .rect(module_length, slit_width)
    .extrude(2)
    .translate((0, -outer_diameter / 2, -1))
)

# === AIR PORT (Top Center) ===
port = (
    cq.Workplane("YZ")
    .circle(port_diameter / 2)
    .extrude(port_depth)
    .translate((0, outer_diameter / 2, module_length / 2))
)

# === HONEYCOMB AERATOR ===
r = hex_size / math.sqrt(3) # point-to-center radius
hex_cell = (
    cq.Workplane("XY")
    .polygon(6, 2 * r)
    .extrude(aerator_thickness)
)

cols = 6
rows = 6
honeycomb = cq.Workplane("XY")
for row in range(rows):
    for col in range(cols):
        x_offset = col * 1.5 * r
        y_offset = row * math.sqrt(3) * r + (col % 2) * math.sqrt(3) * r / 2
        honeycomb = honeycomb.union(hex_cell.translate((x_offset ​:contentReference[oaicite:0]{index=0}​
