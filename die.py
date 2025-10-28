"""Die class for simulating a die roll and displaying the result using ASCII art.

Usage:
    Create a Die object and call the `roll()` method to simulate a die roll.
    The result is printed as a visual representation and returned as an integer.
"""


import random


class Die:
    """Die class simulates a multi-sided die used in games.

    Attributes:
        sides (int): side number of die
    """

    def __init__(self, sides=6):
        """Initialize a Die object.

        Args:
            sides (int, optional): The number of sides on the die. Defaults to 6.
        """
        self.sides = sides

    def roll(self):
        """Simulate rolling the die.

        Returns:
            int: A random integer between 1 and the number of sides.
                If the value is between 1 and 6, an ASCII representation is printed.
        """
        value = random.randint(1, self.sides)
        self.print_die(value)
        return value

    def print_die(self, value):
        """Print an ASCII representation of a die face for values 1 through 6.

        Args:
            value (int): The value to display. Must be between 1 and 6.
        """
        dice_faces = {
            1: ["+-------+",
                "|       |",
                "|   o   |",
                "|       |",
                "+-------+"],
            2: ["+-------+",
                "| o     |",
                "|       |",
                "|     o |",
                "+-------+"],
            3: ["+-------+",
                "| o     |",
                "|   o   |",
                "|     o |",
                "+-------+"],
            4: ["+-------+",
                "| o   o |",
                "|       |",
                "| o   o |",
                "+-------+"],
            5: ["+-------+",
                "| o   o |",
                "|   o   |",
                "| o   o |",
                "+-------+"],
            6: ["+-------+",
                "| o   o |",
                "| o   o |",
                "| o   o |",
                "+-------+"]
        }

        for line in dice_faces.get(value, "Invalid roll"): #.get method on dictionary
            print(line) 


''' 

'''