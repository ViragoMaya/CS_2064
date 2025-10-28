"""
Defines the Planet class for the solar system project.
"""

from math import pi


class Planet:
    '''
    Represents a planet with basic astronomy data 

    Attributes:
        name (str): Planet name 
        mass (float): Mass of the planet in kilograms.
        radius (float): Radius of the planet in kilometers.
        distance_from_sun (float): Distance from sun in million kilometers.
        orbital_period (float): Orbital period in days.
    '''

    def __init__(self,
                 new_name, new_mass, new_radius, new_distance_from_sun, new_orbital_period):
        '''
        Initializes a Planet object.
        
        Args:
            new_name (str): Name of the planet.
            new_mass (float): Mass of planet in kg 
            new_radius(float : Radius on km
            new_distance_from_sun (float): Distance from sun in million km
            new_orbital_period (float): Orbital period in days.
        '''
        self.name = new_name
        self.mass = new_mass
        self.radius = new_radius
        self.distance_from_sun = new_distance_from_sun  #
        self.orbital_period = new_orbital_period
        pass

    def __str__(self):
        '''
        Returns a string representation of the planet's attributes and calculated values.
        
        Returns:
            str: Formatted string of Planet data
        '''

        return (f"{self.name}: Mass={self.mass:.2e} kg, Radius={self.radius} km, "
                f"Distance={self.distance_from_sun} million km, "
                f"Orbital Speed={self.calculate_orbital_speed()} km/s, "
                f"Surface Gravity={self.calculate_surface_gravity()} m/s^2")  
   
    def calculate_orbital_speed(self):
        '''
        Calculates the orbital speed of the planet in km/s.
        
        Returns:
            float: Orbital speed in km/s.'''

        # Simplified orbital speed formula: v = 2πr / T
        r_km = self.distance_from_sun * 1e6  # convert million km to km
        T_sec = self.orbital_period * 24 * 3600  # convert days to seconds
        speed = (2 * pi * r_km) / T_sec
        return round(speed, 2)
    

    def calculate_surface_gravity(self):
        '''
        Calculates the surface gravity of the planet in m/s^2.

        Returns:
            float: Surface gravity in m/s^2.
        '''
        G = 6.67430e-11  # m^3/kg/s^2
        radius_m = self.radius * 1000  # convert km to meters
        gravity = (G * self.mass) / (radius_m ** 2)
        return round(gravity, 2)  # m/s^2
    
    def get_info(self):
        '''
        Returns a dictionary of the planet's attributes and calculated values.

        Returns:
            dict: Dictionary of Planet data 
        '''
        return {"name": self.name,
                "mass": self.mass,
                "radius": self.radius,
                "distance_to_sun": self.distance_from_sun,  #
                "orbital_period": self.orbital_period,
                "orbital_speed": self.calculate_orbital_speed(),
                "surface_gravity": self.calculate_surface_gravity()
                }
    
   
    def planet_type(self):
        '''
         Classifies the planet based on its mass and radius.
    
         Returns:
              str: Type of planet ("Terrestrial", "Gas Giant", "Ice Giant", or "Dwarf Planet")
        '''
        if self.mass > 1e25 and self.radius > 30000:
            return "Gas Giant"
        elif self.mass < 1e24 and self.radius < 7000:
            return "Terrestrial"
        else:
            return "Ice Giant or Unknown"

    def is_habitable(self):
        '''
        Returns True if  the planet is within a habitable zone '
        
        Returns:
            bool: True if habitable, False otherwise.
        '''
        return self.planet_type() == "Terrestrial"





