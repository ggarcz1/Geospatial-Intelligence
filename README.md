# A repository of geospatial intelligence projects, code, and algorithms

Coordinates can be defined via the following:

`from coords import Coords`\
`# 2D`\
`point1 = Coords(39.48719569273062, -76.53854508092664, None)`\
`# 3D`\
`point2 = Coords(39.48886062760044, -76.52274732566815, 534)`\
`print(Coords.rise_run(point1, point2, None))`

Random coordinates can be defined via the following:

`from random_coordinates import Random_Coordinates`\
`Random_coordinates.get_2d()`\
`Random_coordinates.get_3d()`

Utilize the following imports for the associated methods below:

`from physics_methods import Physics`\
`Physics.speed(...)`\
`Physics.velocity(...)`\
`Physics.acceleration(...)`

Space is defined as 50 miles in the US and 62 miles internationally.\
50 miles (80.65 km) = 264000 feet (80650 meters) \
62 miles (100 km) = 327360 feet (100000 meters)
