import math


def get_plane_coordinates():
    # p2 = [100,100]
    p2 = [100,0]
    p2 = [0,100]
    p2 = [100, 30]
    p2 = [300, 200]
    return p2

p1 = [0,0]

p2 = get_plane_coordinates()

if p2[0] - p1[0] == 0:
    angle = 90
else:
    angle = math.atan((p2[1]-p1[1])/(p2[0]-p1[0])) * (180/math.pi)
    angle = round(angle, 1)

if angle > 90:
    print('Past point.')

print(f'{angle} degrees')
