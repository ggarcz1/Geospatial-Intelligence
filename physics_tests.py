from physics_methods import Physics
from units import Units
import unittest


# def velocity(pI, pF, tI, tF):
class TestCoordinateComputations(unittest.TestCase):
    def test_speed_1(self):
        result = Physics.speed(3232, 0, 0)
        self.assertEqual(result, None)

    def test_speed_2(self):
        result = Physics.speed(3232, 4, 8)
        self.assertEqual(result, 3232 / 4)

    def test_speed_3(self):
        result = Physics.speed(12, 0, 4)
        self.assertEqual(result, 3.0)

    def test_speed_4(self):
        result = Physics.speed(3232, -18, 4)
        self.assertEqual(result, None)

    def test_speed_5(self):
        result = Physics.speed(3232, 5, 2)
        self.assertEqual(result, None)

    def test_speed_6(self):
        result = Physics.speed(-999, 5, 2)
        self.assertEqual(result, None)

    def test_velocity_1(self):
        result = Physics.velocity(1, 3232, 0, 0)
        self.assertEqual(result, None)

    def test_velocity_2(self):
        result = Physics.velocity(1, 3232, 4, 8)
        self.assertEqual(result, 807.75)

    def test_velocity_3(self):
        result = Physics.velocity(-32, 12, 0, 4)
        self.assertEqual(result, 11.0)

    def test_velocity_4(self):
        result = Physics.velocity(1, 3232, -18, 4)
        self.assertEqual(result, None)

    def test_velocity_5(self):
        result = Physics.velocity(1, 3232, 5, 2)
        self.assertEqual(result, None)

    def test_acceleration_1(self):
        result = Physics.acceleration(1, 3232, 0, 0)
        self.assertEqual(result, None)

    def test_acceleration_2(self):
        result = Physics.acceleration(1, 3232, 4, 8)
        self.assertEqual(result, 807.75)

    def test_acceleration_3(self):
        result = Physics.acceleration(-32, 12, 0, 4)
        self.assertEqual(result, 11.0)

    def test_acceleration_4(self):
        result = Physics.acceleration(1, 3232, -18, 4)
        self.assertEqual(result, None)

    def test_acceleration_5(self):
        result = Physics.acceleration(1, 3232, 5, 2)
        self.assertEqual(result, None)

    def test_time_1(self):
        u = Units('miles', 'hour')
        result = Physics.time_to_x(5, 5, u.measure_distance, u.measure_time)
        self.assertEqual(result, (1, 'miles/hour'))

    def test_time_2(self):
        u = Units('miles', 'hour')
        result = Physics.time_to_x(3540, 600, u.measure_distance, u.measure_time)
        self.assertEqual(result, (5.9, 'miles/hour'))

    def test_time_3(self):
        u = Units('miles', 'hour')
        result = Physics.time_to_x(6000, 600, u.measure_distance, u.measure_time)
        self.assertEqual(result, (10, 'miles/hour'))

    def test_time_4(self):
        u = Units('meters', 'second')
        result = Physics.time_to_x(6000, 600, u.measure_distance, u.measure_time)
        self.assertEqual(result, (10, 'meters/second'))

    def test_time_5(self):
        u = Units('meters', 'second')
        result = Physics.time_to_x(-999, 600, u.measure_distance, u.measure_time)
        self.assertEqual(result, 'Error: one or more values are less than 0, please check inputs:\n[\'distance\']')

    def test_time_6(self):
        u = Units('meters', 'second')
        result = Physics.time_to_x(999, -600, u.measure_distance, u.measure_time)
        self.assertEqual(result, 'Error: one or more values are less than 0, please check inputs:\n[\'speed\']')

    def test_time_7(self):
        u = Units('meters', 'second')
        result = Physics.time_to_x(-999, -600, u.measure_distance, u.measure_time)
        self.assertEqual(result, 'Error: one or more values are less than 0, '
                                 'please check inputs:\n'+'[\'distance\',\'speed\']')

    def test_units_1(self):
        result = Units('miles', 'hour')
        self.assertEqual(result.__str__(), 'miles/hour')

    def test_units_2(self):
        u = Units('kilometers', 'second')
        result = Units('kilometers', 'second')
        self.assertEqual(result.__str__(), 'kilometers/second')

    def test_units_3(self):
        result = Units(-2323, 213123)
        self.assertEqual(result.__str__(), 'None/None')


if __name__ == '__main__':
    unittest.main()
