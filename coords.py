import math


class Coords:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    # returns a pretty string representation of the coordinates
    def __str__(self):
        return f"Coords(x={self.x}, y={self.y}, z={self.z})"
    
    # returns a list of the coordinates
    def values(self):
        return [self.x, self.y, self.z]
    
    def rise_run(coord1, coord2, coord3):
    # 3d check
        if coord3 == None:
            return (coord2.y-coord1.y)/(coord2.x-coord1.x)
        # TODO:
        else:
            # z is in feet
            return (coord2.y-coord1.y)/(coord2.x-coord1.x)

    def rise(coord1, coord2, coord3):
        # 3d check
        if coord3 == None:
            return coord2.y-coord1.y
        # TODO:
        else:
            return coord2.y-coord1.y

    def run(coord1, coord2, coord3):
        # 3d check
        if coord3 == None:
            return coord2.x-coord1.x
        # TODO:
        else:
            return coord2.x-coord1.x

    def distance_2d(coord1, coord2):
        return math.sqrt((coord2.x-coord1.x)**2+(coord2.y-coord1.y)**2)

    # source: https://chat.openai.com/share/d25da242-c9e8-41ab-ba38-b3c95b9dca91
    def haversine_distance(coord1, coord2, coord3):
        if coord3 == None:
            # must be 2 points in coord1 and coord2 
            if not coord1 == None and not coord2 == None:
                # Convert latitude and longitude from degrees to radians
                lat1 = coord1.x
                lat2 = coord2.x
                lon1 = coord1.y
                lon2 = coord2.y
                lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
                # Haversine formula
                dlat = lat2 - lat1
                dlon = lon2 - lon1
                a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                radius_of_earth = 3958.8  # Earth's radius in miles
                return radius_of_earth * c
            else:
                return None

    def rise_run(coord1, coord2, coord3):
        # 3d check
        if coord3 == None:
            return (coord2.y-coord1.y)/(coord2.x-coord1.x)
        # TODO:
        else:
            return (coord2.y-coord1.y)/(coord2.x-coord1.x)
        