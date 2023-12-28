from coords import Coords
import math
from random_coordinates import Random_Coordinates

c1 = Random_Coordinates()
print(c1.get_pairs())
# def rise_run(coord1, coord2, coord3):
#     # 3d check
#     if coord3 == None:
#         return (coord2.y-coord1.y)/(coord2.x-coord1.x)
#     else:
#         return (coord2.y-coord1.y)/(coord2.x-coord1.x)

# def rise(coord1, coord2, coord3):
#     # 3d check
#     if coord3 == None:
#         return coord2.y-coord1.y
#     else:
#         return coord2.y-coord1.y

# def run(coord1, coord2, coord3):
#     # 3d check
#     if coord3 == None:
#         return coord2.x-coord1.x
#     else:
#         return coord2.x-coord1.x

# def two_points_distance(coord1, coord2):
#     return math.sqrt((coord2.x-coord1.x)**2+(coord2.y-coord1.y)**2)


# # source: https://chat.openai.com/share/d25da242-c9e8-41ab-ba38-b3c95b9dca91
# def haversine_distance(coord1, coord2, coord3):
#     if coord3 == None:
#         # Convert latitude and longitude from degrees to radians
#         lat1 = coord1.x
#         lat2 = coord2.x
#         lon1 = coord1.y
#         lon2 = coord2.y
#         lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
#         # Haversine formula
#         dlat = lat2 - lat1
#         dlon = lon2 - lon1
#         a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
#         radius_of_earth = 3958.8  # Earth radius in miles
#         return radius_of_earth * c
#     else:
#         return 0
    
point1 = Coords(39.48719569273062, -76.53854508092664, None)
point2 = Coords(39.48886062760044, -76.52274732566815, None)

# print(Coords.rise(point1, point2, None))
# print(Coords.run(point1, point2, None))
# print(Coords.rise_run(point1, point2, None))

# # f"{value:.3f}"
# print(f"{Coords.haversine_distance(point1, point2, None):.3f} miles")
