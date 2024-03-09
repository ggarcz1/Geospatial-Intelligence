# A repository of geospatial intelligence projects, code, and algorithms

Coordinates can be defined via the following:

`from coords import Coords`\
`# 2D`\
`point1 = Coords(39.48719569273062, -76.53854508092664, None)`\
`point2 = Coords(39.48886062760044, -76.52274732566815, None)`\
`print(Coords.rise_run(point1, point2, None))`\
`# 3D`\
`point3 = Coords(39.48886062760044, -76.52274732566815, 534)`

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


### ToDo: ###
1. In `coods.py` figure out if the "none" is valid check for the `z` parameter in coordinates.  This may cayse issues with 2D vs 3D point verifications.
  - What about 1D points?
  - Could possibly add a check for the dimension type to the coords class \

See issue at : https://github.com/ggarcz1/Geospatial-Intelligence/issues/7

1. Tracking and vectoring.  See issues below:
   - https://github.com/ggarcz1/Geospatial-Intelligence/issues/5
   - https://github.com/ggarcz1/Geospatial-Intelligence/issues/6