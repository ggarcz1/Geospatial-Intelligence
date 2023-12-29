from coords import Coords
import math
from random_coordinates import Random_Coordinates

c1 = Random_Coordinates()
point1 = c1.get_pair()
point2 = c1.get_pair()
print(point1, point2)
# print(Coords.rise(point1, point2, None))
# print(Coords.run(point1, point2, None))
# print(Coords.rise_run(point1, point2, None))
# # f"{value:.3f}"
print(f"{Coords.haversine_distance(point1, point2, None):.3f} miles")

point3 = c1.get_few()
print(point3)

for count in range (3):
    print(c1.get_few())
