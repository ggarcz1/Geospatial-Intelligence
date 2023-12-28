import random

class Random_Coordinates:
    def get_pairs(self):
        random_long = round(random.uniform(-90, 90), 15)
        random_lat = round(random.uniform(-180, 180), 15)
        return random_long, random_lat
        

# use
# c1 = Random_Coordinates()
# print(c1.get_pairs())