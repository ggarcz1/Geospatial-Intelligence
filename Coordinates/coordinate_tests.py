from coords import Coords
from distances import Distances
import unittest

class TestCoordinateComputations(unittest.TestCase):
    def test_dimension_1(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, 44)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['Error. Dimension is set at 44'])

    def test_dimension_2(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, -2)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['Error. Dimension is set at -2'])

    def test_dimension_3(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, None)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['Error. Dimension is set at None'])

    def test_dimension_4(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, 2.2)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['Error. Dimension is set at 2.2'])

    def test_dimension_5(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, 'hi')
        result = Coords.test_params(point1)
        self.assertEqual(result, ['Error. Dimension is set at hi'])

    # # TODO
    # def test_dimension_6(self):
    #     point1 = Coords(39.48719569273062, -76.53854508092664, None, 2)
    #     result = Coords.test_params(point1)
    #     self.assertEqual(result, ['Error. Dimension is set at 44'])

    def test_range_checks_1(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, 2)
        result = Coords.test_params(point1)
        self.assertEqual(result, '')

    def test_range_checks_2(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, 12432, 3)
        result = Coords.test_params(point1)
        self.assertEqual(result, '')

    def test_range_checks_3(self):
        point1 = Coords(1233213123, -76.53854508092664, 12432, 3)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['X value is out of range -90 to 90'])

    def test_range_checks_4(self):
        point1 = Coords(123321312321, 53854508092664, 12432, 3)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['X value is out of range -90 to 90',
                                  'Y value is out of range -180 to 180'])

    def test_range_checks_5(self):
        point1 = Coords(123321312321, 53854508092664, 3243243243232, 3)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['X value is out of range -90 to 90',
                                  'Y value is out of range -180 to 180',
                                  'Z value is out of range 0 to 264000'])

    def test_range_checks_6(self):
        point1 = Coords('swiz zero', 'hallo', 'france', 3)
        result = Coords.test_params(point1)
        self.assertEqual(result, ['X value is out of range -90 to 90',
                                  'Y value is out of range -180 to 180',
                                  'Z value is out of range 0 to 264000'])

    def test_haversine_dist_two_points_1(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, 2)
        point2 = Coords(39.48886062760044, -76.52274732566815, None, 2)
        result = Distances.haversine_distance(point1, point2)
        self.assertEqual(result, 0.8502160750610919)
        self.assertEqual(round(result, 2), 0.85)

    def test_haversine_dist_two_points_2(self):
        point1 = Coords(41.42751697778474, -75.92733091231945, None, 2)
        point2 = Coords(36.32418982833003, -110.22953052763988, None, 2)
        result = Distances.haversine_distance(point1, point2)
        self.assertEqual(round(result, 2), 1865.86)
        self.assertEqual(result, 1865.8575942399013)

    # should always be 0
    def test_haversine_dist_3_points(self):
        point1 = Coords(0, 0, None, 2)
        point2 = Coords(0, 0, None, 2)
        result = Distances.haversine_distance(point1, point2)
        self.assertEqual(result, 0.0)

    def test_haversine_dist_1_point(self):
        point1 = Coords(39.48719569273062, -76.53854508092664, None, 2)
        point2 = None
        result = Coords.haversine_distance(point1, point2)
        self.assertEqual(result, None)

    def test_haversine_dist_0_point(self):
        point1 = point2 = None
        result = Distances.haversine_distance(point1, point2)
        self.assertEqual(result, None)

    # # distance_2d
    # def test_distance_2d_1(self):
    #     point1 = Coords(41.42751697778474, -75.92733091231945, None, 2)
    #     point2 = Coords(36.32418982833003, -110.22953052763988, None, 2)
    #     result = Coords.distance_2d(point1, point2)
    #     # need to calculate these
    #     self.assertEqual(round(result, 2), 1865.86)
    #     self.assertEqual(result, 1865.8575942399013)

    # def test_distance_2d_2(self):
    #     point1 = Coords(74, 91, None, 2)
    #     point2 = Coords(-123123, 321, None, 2)
    #     result = Coords.distance_2d(point1, point2)
    #     # need to calculate these
    #     self.assertEqual(round(result, 2), 1865.86)
    #     self.assertEqual(result, 1865.8575942399013)

    def test_distance_2d_3_equals_0(self):
        point1 = Coords(74, 91, None, 2)
        point2 = Coords(74, 91, None, 2)
        result = Coords.distance_2d(point1, point2)
        # need to calculate these
        self.assertEqual(round(result, 2), 0)
        self.assertEqual(result, 0)

    def test_distance_2d_4_greater_0(self):
        point1 = Coords(-87654, -8965453, None, 2)
        point2 = Coords(-3424567, -9876543, None, 2)
        result = Coords.distance_2d(point1, point2)
        # need to calculate these
        self.assertGreater(round(result, 2), 0)
        self.assertGreater(result, 0)

    # rise over run   
    def test_rise_over_run_2d_1(self):
        point1 = Coords(-87654, -8965453, None, 2)
        point2 = Coords(-3424567, -9876543, None, 2)
        result = Coords.distance_2d(point1, point2)
        # need to calculate these
        self.assertGreater(round(result, 2), 0)
        self.assertGreater(result, 0)
    
    def test_rise_over_run_2d_2(self):
        point1 = Coords(-87654, -8965453, None, 2)
        point2 = Coords(-3424567, -9876543, None, 2)
        result = Distances.rise_run(point1, point2, None)
        # need to calculate these
        self.assertEqual(result, 0.27303)
    # rise

    # run

if __name__ == '__main__':
    unittest.main()
