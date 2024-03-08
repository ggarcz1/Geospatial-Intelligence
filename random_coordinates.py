import random
from coords import Coords

# 50 miles = 264000 feet
# 62 miles = 327360 feet

# # use
# c1 = Random_Coordinates()
# print(c1.get_pairs())

class Random_Coordinates:
    def get_2d(self) -> Coords:
        random_long = round(random.uniform(-90, 90), 15)
        random_lat = round(random.uniform(-180, 180), 15)
        return Coords(random_long, random_lat, None)
        # return [random_long, random_lat, None]
    

    def get_3d(self) -> Coords:
        random_x = round(random.uniform(-90, 90), 15)
        random_y = round(random.uniform(-180, 180), 15)
        random_z = round(random.uniform(0, 264000), 0)
        return Coords(random_x, random_y, random_z)
        # return [random_x, random_y, random_z]
        