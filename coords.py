import math

RADIUS_EARTH_MILES = 3958.8
class Coords:
    
    def __init__(self, x=0, y=0, z=0, dimension=0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.dimension = dimension

    # returns a pretty string representation of the coordinates
    def __str__(self):
        return f'Coords(x={self.x}, y={self.y}, z={self.z}, Dimension={self.dimension})'

    # returns a list of the full coordinates
    def values(self) -> list:
        return [self.x, self.y, self.z]

    # returns a list of the rounded coordinates
    def rounded_values(self) -> list:
        return [round(self.x), round(self.y), round(self.z)]

    def test_params(point) -> list:
        rtn_text = []
        type_x, type_y, type_z, type_dimension = \
            type(point.x), type(point.y), type(point.z), type(point.dimension)
        dimension = point.dimension

        # TODO: match the number of inputs to the dimensions
        if dimension is None or \
                type_dimension is not int\
                or dimension < 1\
                or dimension > 3:
            return [f'Error. Dimension is set at {dimension}']

        # always need at lest one dimension
        if point.x is None or \
                (type_x is not float
                 and type_x is not int) \
                or (-90 > point.x) \
                or (point.x > 90):
            rtn_text.append('X value is out of range -90 to 90')

        if dimension == 2 or dimension == 3:
            if point.y is None or \
                    (type_y is not float
                     and type_y is not int) \
                    or (-180 > point.y) \
                    or (point.y > 180):
                rtn_text.append('Y value is out of range -180 to 180')

        # TODO: need to figure out if the 'none' is valid check here
        # this may cause issues with 2d vs 3d items.
        # can check this later on if the value is needed
        # OR I can add a type check to the overall coords class parameters
        if dimension == 3:
            if point.z is None or \
                    (type_z is not float
                     and type_z is not int) \
                    or (0 > point.z) \
                    or (point.z > 264000):
                rtn_text.append('Z value is out of range 0 to 264000')

        return rtn_text if len(rtn_text) != 0 else ''

    def rise_run(coord1: float, coord2: float, coord3: float) -> float:
        # 2d check
        if coord3 is None:
            return (coord2.y - coord1.y) / (coord2.x - coord1.x)
        
        math.sqrt((coord2.x - coord1.x) ** 2 
                        + (coord2.y - coord1.y) ** 2
                        + (coord2.z - coord1.z) ** 2)
        # # TODO:
        # else:
        #     # z is in feet
        #     return (coord2.y - coord1.y) / (coord2.x - coord1.x)

    def rise(coord1: float, coord2: float, coord3: float) -> float:
        # 2d check
        if coord3 is None:
            return coord2.y - coord1.y
        return None

    def run(coord1: float, coord2: float, coord3: float) -> float:
        # 2d check
        if coord3 is None:
            return coord2.x - coord1.x
        return None
    
    def distance_2d(coord1: float, coord2: float) -> float:
        return math.sqrt((coord2.x - coord1.x) ** 2 + (coord2.y - coord1.y) ** 2)

    # def rise_run(coord1: float, coord2: float, coord3: float) -> float:
    #     # 2d check
    #     if coord3 is None:
    #         return (coord2.y - coord1.y) / (coord2.x - coord1.x)
    #     return math.sqrt((coord2.x - coord1.x) ** 2 
    #                     + (coord2.y - coord1.y) ** 2
    #                     + (coord2.z - coord1.z) ** 2)


    # this works??
    # called it in main.py
    # source: https://chat.openai.com/share/d25da242-c9e8-41ab-ba38-b3c95b9dca91
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
        return [RADIUS_EARTH_MILES * c]


    def euclidean_distance(coord1: float, coord2: float) -> float:
        distance = math.sqrt((coord2.x - coord1.x)**2 + 
                             (coord2.y - coord1.y)**2 + 
                             (coord2.z - coord1.z)**2)
        return distance

    # def inside_out_coords(coord1: float, coord2: float) -> str:
    #         [0,0]
    #         [0,1]
    #         return 'inside'
    
    def random():
        return -1