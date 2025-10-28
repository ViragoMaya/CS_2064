"""Defines the Star class for the Solar System Project.

Stars are objects within a solar system that have attributes such as name, type, and mass."""

class Star:
    '''
    Represents a star in a solar system with a name, type, and mass(kg)
    
     Attributes:
        name (str): Name of the star.
        mass (float): Mass of the star in kilograms.
        type (str): The classification of the star (e.g., G-type, M-type).
    '''

    def __init__(self, name, mass, type):
        '''
        Initializes a star object.
        
        Args:
            name (str): Name of the star.
            mass (float): Mass of the star in kilograms.
            type (str): Classification of the star (e.g., G-type, M-type).

        '''
        self.name = name  # The name of the star
        self.mass = mass  # in kilograms
        self.type = type  # e.g., G-type, M-type



    def __str__(self):
        '''
        Returns a string representation of the star object.

        Returns:
            str: String with star name, type, and mass.
        '''
        return f"Star {self.name}: Type = {self.type}, Mass = {self.mass:.2e} kg"    