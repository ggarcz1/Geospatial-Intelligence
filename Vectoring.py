import math

class Vectoring:
    def __init__(self):
        return
    
    # p1 is always 0,0 or 0,0,0
    def degrees_calculate(self, p1: list, p2: list) -> float:
        # Calculate the angle using atan2 functions
        angle_radians = math.atan2(p2[1], p2[0])
        # Convert radians to degrees
        angle_degrees = math.degrees(angle_radians)
        # print(angle_degrees)
        vals = {90.0: 0,
                180.0: 270,
                270.0: 180,
                0.0: 90}

        if angle_degrees in vals:
            angle_degrees == vals[angle_degrees]
        elif 0 < angle_degrees < 90:
            angle_degrees = 90 - angle_degrees
        elif 90 < angle_degrees < 180:
            angle_degrees = (180 - angle_degrees) + 270
        # elif angle_degrees > 180 and angle_degrees < 270:
        #     print('here3')
        #     angle_degrees = -999
        else:
            angle_degrees = (270 - angle_degrees) - 180
        return angle_degrees


    def get_nsew(self, degrees: float) -> str:
        degrees %= 360
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
        index = round(degrees / 45) % 8
        return directions[index]


    def get_heading_points(self, heading_degrees):
        # Convert compass heading from degrees to radians
        theta = math.radians(90)  # Polar angle (θ) is 90 degrees
        phi = math.radians(90 - heading_degrees)  # Azimuthal angle (φ) is 90 degrees - compass heading

        # Define radius
        r = 1  # Assuming unit radius for simplicity

        # Calculate Cartesian coordinates using spherical to Cartesian conversion
        x_coordinate = r * math.sin(theta) * math.cos(phi)
        y_coordinate = r * math.sin(theta) * math.sin(phi)
        z_coordinate = r * math.cos(theta)
        return [x_coordinate, y_coordinate, z_coordinate]

    # TODO:
    def plot_vector_to_target(self, p1: list, p2: list) -> float:
        degrees = self.degrees_calculate(p1, p2)

        return 0
        
