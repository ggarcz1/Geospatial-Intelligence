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