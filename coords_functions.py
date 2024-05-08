import math

class Coords_Functions:
    def __init__(self):
        return

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

    def run(self, coord1: float, coord2: float, coord3: float) -> float:
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
    def euclidean_distance(point1, point2):
        """
        Calculate the Euclidean distance between two points in 3D space.

        Args:
        point1 (tuple): Tuple containing the coordinates (x, y, z) of the first point.
        point2 (tuple): Tuple containing the coordinates (x, y, z) of the second point.

        Returns:
        float: The Euclidean distance between the two points.
        """
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        return distance

    def rise_run(coord1: float, coord2: float, coord3: float) -> float:
        # 3d check
        if coord3 is None:
            return (coord2.y - coord1.y) / (coord2.x - coord1.x)
        # TODO:
        else:
            return (coord2.y - coord1.y) / (coord2.x - coord1.x)
