from Vectoring import Vectoring

v = Vectoring()
p1 = [0, 0]
p2 = [10, 5]

degrees = v.degrees_calculate(p1=p1, p2=p2, decimal=0)
heading = v.get_nsew(degrees=degrees)
print(f'Degrees: {degrees}\nHeading: {heading}')
