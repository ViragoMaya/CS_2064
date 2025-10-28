"""Describe the general purpose of this program.

The general purpose of this program is to play a number guessing game with the user
where the numbers are chosen from 1 to 99 pseudo-randomly.

author: Ghazal Tanavade
"""

import random


def game_intro():
    """Displays the game rules and instructions to the player."""
    print("Welcome to Guess My Number🎲🃏")
    print("Try to beat the game and guess the number between 1 and 99.")
    print("After each round, you'll get two guesses and a card"
          " that may give you a hint... or not!"
    )
    print("We play until you win. Good luck!")
    pass

def computer_number():
    """Generates a pseudo-random integer from 1 to 99 for the player to guess."""
    return random.randint(1,99)
    pass

def player_number():
    """Gives feedback comparing the player's guess to the target number."""
    guess = int(input("Enter your guess (1-99):"))
    return guess

def number_feedback(guess, winNum):
    """Provides feedback comparing the guess to the winning number."""
    if guess > winNum:
        print("Too High")
    elif guess < winNum:
        print ("Too Low")
    #else: does nothing

def card_feedback(d_cards, num):
    """Draws a pseudo-random card from the deck and applies its effect."""
    card= random.choice(d_cards)
    print(f"You drew the card: {card}")

    if card == 'New Number':
        newNum = random.randint(1,99)
        print('The number has changed! Mwahahaha ^* 0 *^ ')
        return newNum

    elif card == 'Starts With':
        print(f' Lil hint: the number starts with: {str(num)[0]}')
        return num

    elif card == 'Sum of Digits':
        sum_of_digits = sum(int(d) for d in str(num))
        print(f' The sum of the digits is: {sum_of_digits}')
        return num


    elif card == 'Divisible by 3':
        if num % 3 == 0:
            print("The number IS divisible by 3.")
        else:
            print("The number is NOT divisible by 3")



    elif card == 'I Love Python':
       print(
        "Keep on guessing twin. You're literally right there twin. "
        "Trust me twin🧘"
    )


    elif card == 'Winner!':
        print(
            f"CONGRATULATIONS! You did it. I always believed in you. "
            f"The number was {num} 😇"
        )
        return num

    return num



def main():
    """Describe the general purpose of this program.

    The general purpose of this program is to play a number guessing game.
    Numbers are chosen from 1 to 99 pseudo-randomly.

    author: Ghazal Tanavade
    """
    # Step 1: Ouput the instructions to the player
    game_intro()

    # Step 2: Initialize variables
    win_num = computer_number()
    guesses = 0

    # here are the cards - do not change them
    cards = [
        'New Number', 'Starts With', 'Sum of Digits', 'Divisible by 3', 'I Love Python'
        ]
    deck = random.choices(cards, [.2, .2, .15, .25, .3], k=51)
    deck.append('Winner!')

    # Step 3: game play
    while True:
        for _ in range(2): #2 guesses per round
            guess = player_number()
            guesses += 1
            if guess == win_num:
                print(f'You guessed in {guesses} tries! The number was {win_num}.')
                return # game ends
            number_feedback(guess, win_num)

        win_num = card_feedback(deck, win_num)

# Do not change or add anything below
if '__main__' == __name__:
    main()
