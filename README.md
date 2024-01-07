## A repository of geospatial intelligence projects, code, and algorithms


Coordinates can be defined via the following:


`from coords import Coords`
`point1 = Coords(39.48719569273062, -76.53854508092664, None)`
`point2 = Coords(39.48886062760044, -76.52274732566815, 534)`
`print(Coords.rise_run(point1, point2, None))`


Space is defined at 50 miles in the US and 62 miles internationally.
50 miles (80.65 km) = 264000 feet
62 miles (100 km) = 327360 feet
