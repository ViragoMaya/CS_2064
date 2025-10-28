"""Unit Test for the Planet Class."""

import unittest

from planet import Planet


class TestPlanet(unittest.TestCase):
    """Testing Planet Class."""
    def setUp(self):
        """Creating default Planet Object.

        Remember setUp() will run before each test method.
        """
        self.planet = Planet("Mars",  6.39e23, 3389.5, 227.9, 686.98)

    def test_init(self):
        """Test initialization of Planet attributes."""
        self.assertEqual(self.planet.name, "Mars")
        self.assertEqual(self.planet.mass, 6.39e23)
        self.assertEqual(self.planet.radius, 3389.5)
        self.assertEqual(self.planet.distance_from_sun, 227.9)
        self.assertEqual(self.planet.orbital_period, 686.98)


    def test_str(self):
        """Testing the representation of the Planet object."""
        expected_value = f"Mars: Mass=6.39e+23 kg, Radius=3389.5 km, "
        expected_value += f"Distance=227.9 million km, "
        expected_value += f"Orbital Speed=24.12 km/s, "
        expected_value += f"Surface Gravity=3.71 m/s^2"
        self.assertEqual(str(self.planet), expected_value)

#additional tests made to test planet.py methods

    def test_calculate_orbital_speed(self):
        """Test the calculation of orbital speed."""
        # Calculate manually for Mars (rounded to 2 decimals)
        self.assertAlmostEqual(self.planet.calculate_orbital_speed(), 24.12, places=2)

    def test_calculate_surface_gravity(self):
        """Test the calculation of surface gravity."""
        # Mars should be about 3.71 m/s^2 (rounded)
        self.assertAlmostEqual(self.planet.calculate_surface_gravity(), 3.71, places=2)

    def test_get_info(self):
        """Test the get_info method returns a dictionary with correct keys and values."""
        info = self.planet.get_info()
        self.assertEqual(info["name"], "Mars")
        self.assertEqual(info["mass"], 6.39e23)
        self.assertEqual(info["radius"], 3389.5)
        self.assertEqual(info["distance_to_sun"], 227.9)
        self.assertEqual(info["orbital_period"], 686.98)
        self.assertAlmostEqual(info["orbital_speed"], 24.12, places=2)
        self.assertAlmostEqual(info["surface_gravity"], 3.71, places=2)

    def test_planet_type_terrestrial(self):
        """Test planet_type returns 'Terrestrial' for small planet."""
        self.assertEqual(self.planet.planet_type(), "Terrestrial")

    def test_planet_type_gas_giant(self):
        """Test planet_type returns 'Gas Giant' for large planet."""
        gas_giant = Planet("Jupiter", 1.898e27, 69911, 778.5, 4332.82)
        self.assertEqual(gas_giant.planet_type(), "Gas Giant")

    def test_planet_type_ice_giant_or_unknown(self):
        """Test planet_type returns 'Ice Giant or Unknown' for in-between planet."""
        ice_giant = Planet("Uranus", 8.681e25, 25362, 2871, 30687.15)
        self.assertEqual(ice_giant.planet_type(), "Ice Giant or Unknown")

    def test_is_habitable_true(self):
        """
        Test is_habitable returns True for 'Terrestrial' planet (Mars).
    
        note: 
        Due to assignment requirements, Earth is NOT considered 'Terrestrial' and thus not habitable, 
        even though it is in reality. Hence I'm testing Mars, which fits the This test uses Mars, which fits the assignment's criteria.
        """
        mars = Planet("Mars", 6.39e23, 3389.5, 227.9, 686.98)
        self.assertTrue(mars.is_habitable())

    def test_is_habitable_false(self):
        """Test is_habitable returns False for non-terrestrial planet."""

        jupiter = Planet("Jupiter", 1.898e27, 69911, 778.5, 4332.82)
        self.assertFalse(jupiter.is_habitable())

if "__main__" == __name__:
    unittest.main(argv=[''], verbosity=2, exit=False)

