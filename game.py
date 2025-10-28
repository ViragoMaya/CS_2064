"""Game orchestrates a two-player dice game using the Die and Player classes.

Usage:
    Run this module directly to start a game between two players. The game
    consists of a specified number of rounds, during which each player rolls
    a die and accumulates points. At the end of the game, the player with
    the highest score is declared the winner.
"""

# from <fileName> import <ClassName>
from projects.proj_2.die import Die
from player import Player
#know when to put and not 


class Game:
    """A class to represent a two-player dice game.

    Attributes:
        player1 (Player): Player 1 object
        player2 (Player): Player 2 object
        rounds (int): number of rounds to automaticaly play
        die (Die): mulit-sided die
    """

    def __init__(self, player1_name, player2_name, rounds=5):
        """Initialize the game with two players and a number of rounds.

        Args:
            player1_name (str): Name of the first player.
            player2_name (str): Name of the second player.
            rounds (int, optional): Number of rounds to play. Defaults to 5.
        """
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.rounds = rounds
        self.die = Die(5)

    def play(self):
        """Start and play the game for the specified number of rounds.

        Each player takes a turn per round.
        """
        print("🎲 Starting Dice Game!")
        for round_num in range(1, self.rounds + 1):
            print()
            print( "-------------------------")
            print(f"--- Round {round_num} ---")
            print( "-------------------------")
            self.player1.take_turn(self.die)
            self.player2.take_turn(self.die)
            self.determine_winner()

        self.declare_winner()

    def determine_winner(self):
        """Determines if the sum of the rolls are even or odd and declares a win.

        The default is player1 is even and player2 is odd.
        """
        if (self.player1.roll + self.player2.roll) % 2 == 0: # even or odd -- check w/ defualt 
            self.player1.score += 1
            print(f"{self.player1.name} win ({self.player1.score})")
        else:
            self.player2.score += 1
            print(f"{self.player2.name} win ({self.player2.score})")

    def declare_winner(self):
        """Determine and print the winner based on player scores."""
        print("\n🏁 And the Winner is: ", end='')
        if (self.player1.score > self.player2.score):
            print(f"{self.player1.name} Wins!\n")
        else:
            print(f"{self.player2.name} Wins!\n")

if __name__ == '__main__': #when you import, it runs the code total,  -- only runs if this file is run directly
    game = Game("Sue", "Flay", 3)
    game.play()

#learn how to write tests