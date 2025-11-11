import math, sys
from pathlib import Path

coords_dir = Path(__file__).resolve().parent / "Coordinates"
sys.path.insert(0, str(coords_dir))
from coords import Coords

random_coords_dir = Path(__file__).resolve().parent / "Random_Coordinates"
sys.path.insert(0, str(random_coords_dir))
from random_coordinates import Random_Coordinates

physics_dir = Path(__file__).resolve().parent / "Physics"
sys.path.insert(0, str(physics_dir))
from distances import Distances

# Get random coordinates
c1 = Random_Coordinates()
point1 = c1.get_3d()
point2 = c1.get_3d()
point3 = c1.get_3d()

dist = Distances.haversine_distance(point1, point2)
print(f'Point 1: {point1.rounded_values()}\nPoint 2: {point2.rounded_values()}')
print(f'{dist:,.2f} miles')

# point3 = c1.get_3d()
# print(point3)

# for count in range (3):
#     print(c1.get_3d())

