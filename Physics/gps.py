import requests


class GPS:
    def __init__(self, name='GPS1', x=0, y=0, z=0, dimension=0) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    # returns a pretty string representation of the coordinates
    def __str__(self):
        return f'GPS(name={self.name},x={self.x},y={self.y},z={self.z})'

    # returns a list of the full coordinates
    def values(self) -> list:
        return [self.name, self.x, self.y, self.z]


