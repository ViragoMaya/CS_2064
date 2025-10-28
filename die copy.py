# Assuming you have a file named die.py with a Die class
from die import Die

class TwoDice:
    """A class to represent a pair of dice."""

    def __init__(self, sides=6):
        """Initializes two Die objects."""
        self.dice1 = Die(sides)
        self.dice2 = Die(sides)

    def roll(self):
        """Rolls both dice and returns their values as a tuple."""
        return (self.dice1.roll(), self.dice2.roll())

    def __str__(self):
        """
        Provides a string representation of a single roll, its total,
        and avoids rolling the dice more than once.
        """
        # Call roll() once and store the result in a variable
        current_roll = self.roll()
        # Use the variable to display the roll and calculate the sum
        return f'Roll: {current_roll}\nTotal: {sum(current_roll)}'

# Example of how to use the class
if __name__ == "__main__":
    two_dice = TwoDice()
    # Printing the object automatically calls the __str__ method
    print(two_dice)

    print("-" * 10)

    # You can still call roll() directly if you only need the tuple
    a_roll = two_dice.roll()
    print(f"Just the roll tuple: {a_roll}")