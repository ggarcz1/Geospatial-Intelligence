import math

# class TimeToTarget:
#     def __init__(self, target: list, velocity: float, acceleration: float) -> None:
#         self.target = target
#         self.velocity = velocity
#         self.acceleration = acceleration


#     def get_time(self):
#         time = 0.0
        
#         distance =         
#         return time

#units are checked and stripped prior
def get_time(distance, speed):

    time = round(distance/speed, 1)

    return time


# print(get_time([0,0,0], 30, 0) == 0)
miles = 123
speed = 10
time = get_time(miles, speed, 0)
print(f'{miles} miles\n{time} seconds')