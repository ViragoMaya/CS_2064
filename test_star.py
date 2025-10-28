"""Unit tests for the Star class from the star_soln module."""

import unittest

from star import Star


class TestStar(unittest.TestCase):
    """Testing the Star class."""

    def setUp(self):
        """Create a Star instance for use in all test methods."""
        self.star = Star("Proxima Centauri", 2.428e29, 'M-type')

    # test the __str__ method
    def test_str(self):
        """Test the __str__ method, returning the correct string ."""
        expected = "Star Proxima Centauri: Type = M-type, Mass = 2.43e+29 kg"
        self.assertEqual(str(self.star), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
