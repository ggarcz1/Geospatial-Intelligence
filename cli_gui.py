import argparse
import math
import random


# calculate the endpoint based on angle and distance given
def calculate_endpoint(angle_degrees: float, distance):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate endpoint coordinates
    end_point_x = 0 + distance * math.cos(angle_radians)
    end_point_y = 0 + distance * math.sin(angle_radians)

    return [end_point_x, end_point_y]

def get_nsew(degrees: float) -> str:
    degrees %= 360
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    index = round(degrees / 45) % 8
    return directions[index]

# TODO: test this
def degrees_calculate(p1: list, p2: list) -> float:
    # Calculate the angle using atan2 functions
    angle_radians = math.atan2(p2[1], p2[0])
    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    vals = {90.0: 0,
            180.0: 270,
            270.0: 180,
            0.0: 90}

    if angle_degrees in vals:
        angle_degrees == vals[angle_degrees]
    elif angle_degrees > 0 and angle_degrees < 90:
        angle_degrees = 90 - angle_degrees
    elif angle_degrees > 90 and angle_degrees < 180:
        angle_degrees = (180 - angle_degrees) + 270
    # elif angle_degrees > 180 and angle_degrees < 270:
    #     print('here3')
    #     angle_degrees = -999
    else:
        angle_degrees = (270 - angle_degrees) - 180

    # determine quadrant
    quarter = quadrant(p2)
    direction = get_nsew(angle_degrees)
    # print(f'Angle: {int(angle_degrees)}\nQuadrant: {quarter}\nDirection: {direction}')

    return angle_degrees

# to calculate the distance of a vector, aka to a "target", point or object
def rise_run(p1: list, p2: list) -> float:
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def distance(p1: list, p2: list) -> float:
    return math.sqrt(
        math.pow(p1[0] - p2[0], 2) +
        math.pow(p1[1] - p2[1], 2))

# for compass directions
# TODO: what if it is on the y or x axis?
def quadrant(point):
    # I
    # x+ y+
    if point[0] > 0 and point[1] > 0:
        return 1
    # II
    # x+ y-
    elif point[0] > 0 and point[1] < 0:
        return 2
    # III
    # x- y-
    elif point[0] < 0 and point[1] < 0:
        return 3
    # IV
    # x+ y-
    else:
        return 4



# usage
# python .\gui_test.py
# python .\gui_test.py -i 2
# python .\cli_gui.py -x 90 -y 3 

parser = argparse.ArgumentParser(description='description')

parser.add_argument('-x', '--arg1', help='x value')
parser.add_argument('-y', '--arg2', help='y value')
parser.add_argument('-i', '--arg3', help='iterations')

args = parser.parse_args()

x = y = i =None

if args.arg1:
    x = float(args.arg1)
    
if args.arg2:
    y = float(args.arg2)

if args.arg3:
    i = int(args.arg3)

# will always be [0, 0]
origin = [0, 0]
# target items
if x == None or y == None:
    target = [random.uniform(-100, 100), random.uniform(-100, 100)]
else:
    target = [x, y]
    i = 1

# no input supplied, run it once
if i is None:
    i = 1

print('----------------')
for each in range(0, i):
    target = [random.uniform(-100, 100), random.uniform(-100, 100)]
    dist = distance([0, 0], target)
    dst = round(dist, 2)
    dgr = round(degrees_calculate(origin, target), 2)
    direct = get_nsew(dgr)
    q = quadrant(target)
    print(f'Target: {target}\nDistance: {dst}\nDegrees: {dgr}\nDirection: {direct}\nQuadrant: {q}\n----------------')

msg = 'Done'
print(f'\n\n--------Message--------\n\t {msg}\n-----------------------')
