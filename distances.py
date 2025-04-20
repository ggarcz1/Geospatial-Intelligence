from coords import Coords
from units import Units
import math

RADIUS_EARTH_MILES = 3958.8

class Distances:
    
    def rise_run(coord1: Coords, coord2: Coords, coord3: Coords) -> float:
        # 2d check
        if coord3 is None:
            return round((coord2.y - coord1.y) / (coord2.x - coord1.x), 5)
        
        math.sqrt((coord2.x - coord1.x) ** 2 
                        + (coord2.y - coord1.y) ** 2
                        + (coord2.z - coord1.z) ** 2)
        # # TODO:
        # else:
        #     # z is in feet
        #     return (coord2.y - coord1.y) / (coord2.x - coord1.x)

    def rise(coord1: Coords, coord2: Coords, coord3: Coords) -> float:
        # 2d check
        if coord3 is None:
            return coord2.y - coord1.y
        return None

    def run(coord1: Coords, coord2: Coords, coord3: Coords) -> float:
        # 2d check
        if coord3 is None:
            return coord2.x - coord1.x
        return None
    
    def distance_2d(coord1: Coords, coord2: Coords) -> float:
        return math.sqrt((coord2.x - coord1.x) ** 2 + (coord2.y - coord1.y) ** 2)

    # def rise_run(coord1: float, coord2: float, coord3: float) -> float:
    #     # 2d check
    #     if coord3 is None:
    #         return (coord2.y - coord1.y) / (coord2.x - coord1.x)
    #     return math.sqrt((coord2.x - coord1.x) ** 2 
    #                     + (coord2.y - coord1.y) ** 2
    #                     + (coord2.z - coord1.z) ** 2)


    # distance between 2 objects on a sphere
    def haversine_distance(coord1: Coords, coord2: Coords) -> list:
        if coord1 is None or coord2 is None:
            return
        
        # Convert latitude and longitude from degrees to radians
        lat1 = coord1.x
        lat2 = coord2.x
        lon1 = coord1.y
        lon2 = coord2.y
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        # radius_of_earth = 3958.8  # Earth's radius in miles
        return (RADIUS_EARTH_MILES * c)

    # distance between 2 objects on a 2-D plane
    def euclidean_distance(coord1: float, coord2: float) -> float:
        distance = math.sqrt((coord2.x - coord1.x)**2 + 
                             (coord2.y - coord1.y)**2 + 
                             (coord2.z - coord1.z)**2)
        return distance

    # def inside_out_coords(coord1: float, coord2: float) -> str:
    #         [0,0]
    #         [0,1]
    #         return 'inside'
