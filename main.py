from coords import Coords
import math
from random_coordinates import Random_Coordinates

c1 = Random_Coordinates()
point1 = c1.get_3d()
point2 = c1.get_3d()
point3 = c1.get_3d()
dist = Coords.haversine_distance(point1, point2)
print(f'Point 1: {point1.rounded_values()}\nPoint 2: {point2.rounded_values()}')
print(f'{dist[0]:.2f} miles')

# point3 = c1.get_3d()
# print(point3)

# for count in range (3):
#     print(c1.get_3d())

