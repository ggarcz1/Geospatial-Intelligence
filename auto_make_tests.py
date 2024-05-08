
def get_thing(angle_degrees):
    vals = {90.0: 0.0,
            180.0: 270.0,
            270.0: 180.0,
            0.0: 90.0}

    if angle_degrees in vals:
        return vals[angle_degrees]
    elif angle_degrees > 0 and angle_degrees < 90:
        angle_degrees = 90 - angle_degrees
    elif angle_degrees > 90 and angle_degrees < 180:
        angle_degrees = (180 - angle_degrees) + 270
    elif angle_degrees > 180 and angle_degrees < 270:
        angle_degrees = -999
    else:
        angle_degrees = (270 - angle_degrees) - 180

    return angle_degrees


counter_compass = 0
counter_graph = 90

# NSEW Value, math value 
counter = 0.0
while counter <= 90:
    print(counter, get_thing(counter))
    counter += 1.0

counter = 90.0
while counter <= 180:
    print(counter, get_thing(counter))
    counter += 1.0

counter = 180.0
while counter <= 270:
    print(counter, get_thing(counter))
    counter += 1.0

counter = 270.0
while counter <= 360:
    print(counter, get_thing(counter))
    counter += 1.0


def get_nsew(degrees: float) -> str:
    degrees %= 360
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    index = round(degrees / 45) % 8
    return directions[index]

counter = 0
while counter <= 360:
    print(counter, get_thing(counter), get_nsew(get_thing(counter)))
    counter += 1

# string = f'\tdef test_vals(self):'\
#         f'\n\t\tresult = Physics.speed(3232, 0, 0)'\
#         f'\n\t\tself.assertEqual({counter_compass}, {counter_graph})'

# print(string)