import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import random
import argparse
# from coords import Coords


# usage:
# python .\3d_gui_gpt.py -x 10 -y 13 -z 14 -d 83
# -x --> x point of target
# -y --> y point of target
# -z --> z point of target
# -d --> direction of origin

# for default hardcoded values
# python .\3d_gui_gpt.py 

def degrees_calculate(p1: list, p2: list) -> float:
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


def get_nsew(degrees: float) -> str:
    degrees %= 360
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    index = round(degrees / 45) % 8
    return directions[index]


def plot_arrow(ax, x, y, z, color):
    ax.quiver(0, 0, 0, x, y, z, color=color, arrow_length_ratio=0.1)


def get_heading_points(heading_degrees):
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


parser = argparse.ArgumentParser(description='description')
parser.add_argument('-x', '--arg1', help='x')
parser.add_argument('-y', '--arg2', help='y')
parser.add_argument('-z', '--arg3', help='z')
parser.add_argument('-d', '--arg4', help='directional heading')

x_point = y_point = z_point = 0

args = parser.parse_args()
if args.arg1 and args.arg2 and args.arg3 and args.arg4:
    x_point = float(args.arg1)
    y_point = float(args.arg2)
    z_point = float(args.arg3)
    heading_origin = float(args.arg4)

else:
    x_point = 10
    y_point = -15
    z_point = -6
    heading_origin = 283

# distance = Coords.euclidean_distance([0, 0, 0], [x_point, y_point, z_point])

distance = math.sqrt((x_point - 0)**2 + (y_point - 0)**2 + (z_point - 0)**2)

target = [x_point, y_point, z_point]
# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the point at (0, 0)
ax.scatter(0, 0, 0, color='blue', label='')

# Plot the user-supplied point
ax.scatter(x_point, y_point, z_point, color='green', label='Target')
ax.scatter(0, 0, 0, color='Blue', label='Origin Direction')
ax.scatter(0, 0, 0, color='White', label=f'{heading_origin} - {get_nsew(heading_origin)}')
ax.scatter(0, 0, 0, color='White', label=f'{round(distance)} Miles')


# Plot the arrow from (0, 0) to the target
plot_arrow(ax, x_point, y_point, z_point, color='red')

# Plot the arrow for N, S, E, W
# if z_point <= 0:
#     z_point -= 5
# else:
#     z_point += 5

z_point = 6
len_compass = abs(min(x_point, y_point, z_point) / 2)
len_compass = 6
ax.quiver(0, 0, z_point, 0, len_compass, 0, color='black')
ax.text(0, len_compass+1, z_point, 'N', color='Black')
ax.quiver(0, 0, z_point, 0, -len_compass, 0, color='black')
ax.text(0, -(len_compass+1), z_point, 'S', color='Black')
ax.quiver(0, 0, z_point, len_compass, 0, 0, color='black')
ax.text(len_compass+1, 0, z_point, 'E', color='Black')
ax.quiver(0, 0, z_point, -len_compass, 0, 0, color='black')
ax.text(-(len_compass+1), 0, z_point, 'W', color='Black')

# direction of travel for origin
target_degrees = degrees_calculate([0, 0], [x_point, y_point])
nsew_target = get_nsew(degrees=target_degrees)
nsew_origin = get_nsew(degrees=heading_origin)
# target direction and degrees
ax.scatter(0, 0, 0, color='White', label=f'Target: {round(target_degrees)} - {get_nsew(target_degrees)}')

# direction of travel for origin, static coordinate plaes
points = get_heading_points(heading_degrees=heading_origin)
# print(points)
plot_arrow(ax, points[0] * 10, points[1] * 10, points[2] * 10, color='blue')

# empty space
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])

target[0] = round(target[0])
target[1] = round(target[1])
target[2] = round(target[2])
ax.set_title(f'Arrow from origin (0, 0, 0) to Target at {target} relative')
ax.text(x_point, y_point, z_point, "Target", color='red')


# Show plot
plt.legend()
plt.show()
