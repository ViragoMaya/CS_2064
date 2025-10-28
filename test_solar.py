"""Unit tests for the SolarSystem class."""

import unittest

from planet import Planet
from solar_system import SolarSystem

class TestSolar(unittest.TestCase):

    def setUp(self):
        """
        Initializing a Solar System object.
        
        Remember that setUP() is run before each test method.
        """
        self.solar_sys = SolarSystem("Zed", "Zamp")
#own test 
    def test_init(self):
        """
        Test initialization of SolarSystem attributes.
        """
        self.assertEqual(self.solar_sys.name, "Zed")
        self.assertEqual(self.solar_sys.star, "Zamp")
        self.assertEqual(len(self.solar_sys.planets), 0)

    def test__str(self):
        """
        Verifies that the string representation of a SolarSystem object.
        """
        p = Planet("P", 1, 1, 1, 1)
        self.solar_sys.add_planet(p)
 
        expected_value = "Zed:\n  Zamp\n  "
        expected_value += "P: Mass=1.00e+00 kg, Radius=1 km, Distance=1 million km, Orbital Speed=72.72 km/s Surface Gravity=0.0  m/s^2\n\n"
        self.assertEqual(str(self.solar_sys), expected_value)

    def test_list_planets(self):
        """
        Verifies when the list is empty and has 1 element.
        """
        result = self.solar_sys.list_planets()
        self.assertEqual(len(result), 0)
        z_planet = Planet("z", 1, 2, 3, 4)
        self.solar_sys.add_planet(z_planet)
        result = self.solar_sys.list_planets()
        self.assertEqual(result, ['z'])


    # More tests  added to thoroughly test solar_system.py

    
    def test_add_planet(self):
        """
        Test adding a planet to the solar system.

        Returns:
            bool: True if the planet was added, False if it was already there
        """
        p = Planet("P", 1, 1, 1, 1)
        result = self.solar_sys.add_planet(p)
        self.assertTrue(result)
        self.assertIn(p, self.solar_sys.planets)

    def test_add_planet_duplicate(self):
        """
        Tests  adding the same planet twice returns False the second time.
        """
        p = Planet("P", 1, 1, 1, 1)
        self.solar_sys.add_planet(p)
        result = self.solar_sys.add_planet(p)
        self.assertFalse(result)
        self.assertEqual(len(self.solar_sys.planets), 1)

    def test_find_habitable_planets(self):
        """
        Tests finding habitable planets in the solar system.
        Utilizes the assignment logic: mass < 1e24 and radius < 7000 is "terrestrial"/habitable

        """
        p_hab = Planet("Hab", 5e23, 3000, 1, 1)
        p_non = Planet("Gas", 1e26, 50000, 100, 100)
        self.solar_sys.add_planet(p_hab)
        self.solar_sys.add_planet(p_non)
        habitable = self.solar_sys.find_habitable_planets()
        self.assertIn("Hab", habitable)
        self.assertNotIn("Gas", habitable)

    

if "__main__" == __name__:
    unittest.main(argv=[''], verbosity=2, exit=False)
