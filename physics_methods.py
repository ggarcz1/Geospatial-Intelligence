import math
from units import Units


class Physics:
    # def __init__(self, displacement, time):
    #     self.displacement = displacement
    #     self.time = time

    # NOTE: both formulas use the same computation, however,
    # one uses displacement and the other uses velocity as the numerator

    # time unit is dependent on the 
    def time_to_x(distance: float, speed: float, unit_speed: Units, unit_time: float) -> list:
        time = 0
        # distance
        time = distance / speed

        zero_values = []
        if distance < 0:
            zero_values.append('distance')
        if speed < 0:
            zero_values.append('speed')

        if len(zero_values) > 0:
            return f'Error: one or more values are less than 0, please check inputs:\n{zero_values}'

        unit = Units(unit_speed, unit_time)
        return time, unit.__str__()

    # covered in the coords class
    def distance(value1: float, value2: float) -> float:
        if value2 < value1:
            return None

        return value2 - value1

    def speed(distance: float, timeInitial: float, timeFinal: float) -> float:
        # change in distance
        # over
        # change in time
        if (timeFinal - timeInitial) == 0 or distance < 0 or timeInitial > timeFinal or timeInitial < 0:
            return None

        return distance / (timeFinal - timeInitial)

    def velocity(posInitial: float, posFinal: float, timeInitial: float, timeFinal: float) -> float:
        # change in pos
        # over
        # change in time
        if (timeFinal - timeInitial) == 0 or timeInitial > timeFinal or timeInitial < 0:
            return None

        return (posFinal - posInitial) / (timeFinal - timeInitial)

    def acceleration(velocityInitial: float, velocityFinal: float, timeInitial: float, timeFinal: float) -> float:
        # change in velocity
        # over 
        # change in time
        if (timeFinal - timeInitial) == 0 or timeInitial > timeFinal or timeInitial < 0:
            return None

        return (velocityFinal - velocityInitial) / (timeFinal - timeInitial)
