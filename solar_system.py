'''Defines the SolarSystem class for the solar system project.'''

class SolarSystem:
    '''
    Represents a solar system with a name, a central star, and a set of planets.

    Attributes:
        name (str): The name of the solar system
        star (Star): A Star object representing the central star
        planets (set): An empty set to store Planet objects
    '''

    def __init__(self, name, star):
       '''
       Iniitializes SolarSystem Object

       Args:
            new_name (str): Name of the solar system
            new_star (Star): The central star object
       '''
       self.name = name
       self.star = star
       self.planets = set()


    def __str__(self):
        '''
        Returns string representation of Solar Sytstem, listing its stars and plantes

        Returns:
            str: Formatted string with solar system details
        '''

        result = f'{self.name}:\n  {self.star}\n'
        for planet in self.planets:
            result += (f"  {planet.name}: Mass={planet.mass:.2e} kg, Radius={planet.radius} km, "
                    f"Distance={planet.distance_from_sun} million km, "
                    f"Orbital Speed={planet.calculate_orbital_speed()} km/s "
                    f"Surface Gravity={planet.calculate_surface_gravity()}  m/s^2\n\n")
        return result
    

    def list_planets(self):
        '''
        Returns list of planet names in teh solar system

        Returns:
            list: List of all planet names
        '''
        return [planet.name for planet in self.planets]

    def add_planet(self, planet):
        '''
        Adds a Planet object to the solar system's set

        Args:
            planet (Planet): The Planet object to add

        Returns:
            bool: True if the planet was added, False if it was already there
        '''
        if planet in self.planets:
           return False
        self.planets.add(planet)
        return True  


    
    def find_habitable_planets(self):
        '''
        Finds and returns all habitable planets in the solar system

        Returns:
            list: List of names of habitable planets
        '''

        return [planet.name for planet in self.planets if planet.is_habitable()]

    