import math


class Coords:
    def __init__(self, x=0, y=0, z=0, dimension=0):
        self.x = x
        self.y = y
        self.z = z
        self.dimension = dimension

    # returns a pretty string representation of the coordinates
    def __str__(self):
        return f"Coords(x={self.x}, y={self.y}, z={self.z}, Dimension={self.dimension})"

    # returns a list of the coordinates
    def values(self) -> list:
        return [self.x, self.y, self.z]

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

        # TODO: need to figure out if the "none" is valid check here
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

        return rtn_text if len(rtn_text) is not 0 else ''

    def rise_run(coord1: float, coord2: float, coord3: float) -> float:
        # 3d check
        if coord3 is None:
            return (coord2.y - coord1.y) / (coord2.x - coord1.x)
        # TODO:
        else:
            # z is in feet
            return (coord2.y - coord1.y) / (coord2.x - coord1.x)

    def rise(coord1: float, coord2: float, coord3: float) -> float:
        # 3d check
        if coord3 is None:
            return coord2.y - coord1.y
        # TODO:
        else:
            return coord2.y - coord1.y

    def run(coord1: float, coord2: float, coord3: float) -> float:
        # 3d check
        if coord3 is None:
            return coord2.x - coord1.x
        # TODO:
        else:
            return coord2.x - coord1.x

    def distance_2d(coord1: float, coord2: float) -> float:
        return math.sqrt((coord2.x - coord1.x) ** 2 + (coord2.y - coord1.y) ** 2)

    # source: https://chat.openai.com/share/d25da242-c9e8-41ab-ba38-b3c95b9dca91
    def haversine_distance(coord1: float, coord2: float, coord3: float) -> float:
        if coord3 is None:
            # must be 2 points in coord1 and coord2 
            if coord1 is not None and coord2 is not None:
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
                radius_of_earth = 3958.8  # Earth's radius in miles
                return radius_of_earth * c
            else:
                return None

    def rise_run(coord1: float, coord2: float, coord3: float) -> float:
        # 3d check
        if coord3 is None:
            return (coord2.y - coord1.y) / (coord2.x - coord1.x)
        # TODO:
        else:
            return (coord2.y - coord1.y) / (coord2.x - coord1.x)
