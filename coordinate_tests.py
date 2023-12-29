from coords import Coords
import unittest

class TestCoordinateComputations(unittest.TestCase):
    def test_haversine_dist_two_points_1(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None)
        point2 = Coords(39.48886062760044, -76.52274732566815, None)
        point3 = None
        result = Coords.haversine_distance(point1, point2, point3)
        self.assertEqual(result, 0.8502160750610919)
        self.assertEqual(round(result, 2), 0.85)
    
    def test_haversine_dist_two_points_2(self):
        point1 = Coords(41.42751697778474, -75.92733091231945, None)
        point2 = Coords(36.32418982833003, -110.22953052763988, None)
        point3 = None
        result = Coords.haversine_distance(point1, point2, point3)
        self.assertEqual(round(result, 2), 1865.86)
        self.assertEqual(result, 1865.8575942399013)

    # should always be 0
    def test_haversine_dist_3_points(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None)
        point2 = Coords(39.48886062760044, -76.52274732566815, None)
        point3 = Coords(37.48886062760044, -77.52274732566815, None)
        result = Coords.haversine_distance(point1, point2, point3)
        self.assertEqual(result, None)
    
    def test_haversine_dist_1_point(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None)
        point2 = point3 = None
        result = Coords.haversine_distance(point1, point2, point3)
        self.assertEqual(result, None)

    def test_haversine_dist_0_point(self):
        point1 = point2 = point3 = None
        result = Coords.haversine_distance(point1, point2, point3)
        self.assertEqual(result, None)

    # distance_2d
    def test_distance_2d_1(self):
        point1 = Coords(41.42751697778474, -75.92733091231945, None)
        point2 = Coords(36.32418982833003, -110.22953052763988, None)
        result = Coords.distance_2d(point1, point2)
        # need to calculate these
        self.assertEqual(round(result, 2), 1865.86)
        self.assertEqual(result, 1865.8575942399013)

    def test_distance_2d_2(self):
        point1 = Coords(74, 91, None)
        point2 = Coords(-123123, 321, None)
        result = Coords.distance_2d(point1, point2)
        # need to calculate these
        self.assertEqual(round(result, 2), 1865.86)
        self.assertEqual(result, 1865.8575942399013)


    # rise over run   
    # rise
    # run
    # distance_2d
        
    # def test_haversine_dist_3_points(self):
    #     point1 = Coords(39.48719569273062, -76.53854508092664, None)
    #     point2 = Coords(39.48886062760044, -76.52274732566815, None)
    #     point3 = Coords(37.48886062760044, -77.52274732566815, None)
    #     result = Coords.haversine_distance(point1, point2, point3)
    #     self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
