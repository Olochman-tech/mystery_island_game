import unittest
from game import calculate_energy


class TestEnergy(unittest.TestCase):

    def test_energy_reduction(self):
        self.assertEqual(calculate_energy(5, 2), 3)

    def test_energy_reduction_by_one(self):
        self.assertEqual(calculate_energy(3, 1), 2)

    def test_energy_cannot_be_negative(self):
        self.assertEqual(calculate_energy(3, 5), 0)


if __name__ == "__main__":
    unittest.main()