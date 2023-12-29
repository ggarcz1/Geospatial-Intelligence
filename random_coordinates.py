import random
from coords import Coords

class Random_Coordinates:
    def get_pair(self):
        random_long = round(random.uniform(-90, 90), 15)
        random_lat = round(random.uniform(-180, 180), 15)
        return Coords(random_long, random_lat, None)
        # return [random_long, random_lat, None]
    
    # need to look at the z here, if its even practical.  
    # maybe it is altituide above sea level?
    # 50 miles is US
    # 264000 feet
    # Kármán line is often defined to be located 
    # at an altitude of 100 kilometers (62 miles) above Earth's sea level
    # 50 miles = 264000 feet
    # 62 miles = 327360 feet
    def get_few(self):
        random_x = round(random.uniform(-90, 90), 15)
        random_y = round(random.uniform(-180, 180), 15)
        random_z = round(random.uniform(0, 264000), 0)
        return Coords(random_x, random_y, random_z)
        # return [random_x, random_y, random_z]
        
# use
# c1 = Random_Coordinates()
# print(c1.get_pairs())