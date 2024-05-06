
counter_compass = 0
counter_graph = 90
def get_thing(angle_degrees):
    vals = {90.0: 0,
            180.0: 270,
            270.0: 180,
            0.0: 90}
    print(vals[angle_degrees])

    if angle_degrees in vals:
        return angle_degrees == vals[angle_degrees]
    elif angle_degrees > 0 and angle_degrees < 90:
        angle_degrees = 90 - angle_degrees
    elif angle_degrees > 90 and angle_degrees < 180:
        angle_degrees = (180 - angle_degrees) + 270
    # elif angle_degrees > 180 and angle_degrees < 270:
    #     print('here3')
    #     angle_degrees = -999
    else:
        angle_degrees = (270 - angle_degrees) - 180

    return angle_degrees

# counter = 0.0
# while counter <= 360:
#     print(counter, get_thing(counter))
#     counter += 1.0

print(get_thing(90.0))

# string = f'\tdef test_vals(self):'\
#         f'\n\t\tresult = Physics.speed(3232, 0, 0)'\
#         f'\n\t\tself.assertEqual({counter_compass}, {counter_graph})'

# print(string)