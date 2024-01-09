from physics_methods import Physics
import unittest

# def velocity(pI, pF, tI, tF):
class TestCoordinateComputations(unittest.TestCase):
    def test_speed_1(self):
        result = Physics.speed(3232, 0, 0)
        self.assertEqual(result, None)

    def test_speed_2(self):
        result = Physics.speed(3232, 4, 8)
        self.assertEqual(result, 3232/4)

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

if __name__ == '__main__':
    unittest.main()
