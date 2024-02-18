import math
from units import Units

class Physics:  
    # def __init__(self, displacement, time):
    #     self.displacement = displacement
    #     self.time = time

    # NOTE: both formulas use the same computation, however,
    # one uses displacement and the other uses velocity as the numerator
    
    # time unit is dependent on the 
    def time_to_x(distance, speed, unit_speed, unit_time):
        time = 0
        # distance
        time = distance / speed

        if distance < 0 or speed < 0:
            return 'Error: one or more values are less than 0, please check inputs'
        
        unit = Units(unit_speed, unit_time)
        return time, unit.__str__()
    

    # covered in the coords class
    def distance(value1, value2):
        if value2 < value1:
            return None
        
        return value2 - value1
    
    def speed(distance, tI, tF):
        if (tF - tI) == 0 or distance < 0 or tI > tF or tI < 0:
            return None
        
        return distance/(tF-tI)
    
    def velocity(pI, pF, tI, tF):
        # change in pos
        # over
        # change in time
        if (tF - tI) == 0 or tI > tF or tI < 0:
            return None

        return (pF-pI)/(tF-tI)

    def acceleration(vI, vF, tI, tF):
        # change in velocity
        # over 
        # change in time
        if (tF - tI) == 0 or tI > tF or tI < 0:
            return None
        
        return (vF-vI)/(tF-tI)