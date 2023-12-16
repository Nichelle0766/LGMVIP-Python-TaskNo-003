# -*- coding: utf-8 -*-
"""CREATE A ROCK PAPER SCISSORS GAME USING PYTHON

## Rock Paper Scissors Game in Python

Here's a Python code for a simple Rock Paper Scissors game:
"""

import random

# List of possible choices
choices = ["Rock", "Paper", "Scissors"]

# Get player's choice
player_choice = input("Choose Rock, Paper, or Scissors: ").lower()

# Generate computer's choice
computer_choice = random.choice(choices).lower()

# Compare choices and determine winner
winner = None

if player_choice == computer_choice:
    winner = "Tie"
elif player_choice == "rock":
    if computer_choice == "paper":
        winner = "Computer"
    else:
        winner = "Player"
elif player_choice == "paper":
    if computer_choice == "scissors":
        winner = "Computer"
    else:
        winner = "Player"
elif player_choice == "scissors":
    if computer_choice == "rock":
        winner = "Computer"
    else:
        winner = "Player"
else:
    winner = "Invalid choice"

# Display results
if winner == "Tie":
    print(f"It's a tie! Both chose {player_choice}.")
else:
    print(f"{winner.capitalize()} wins! {player_choice.upper()} vs. {computer_choice.upper()}.")

# Play again option
play_again = input("Play again? (y/n): ").lower()

while play_again == "y":
    # Get player's choice
    player_choice = input("Choose Rock, Paper, or Scissors: ").lower()

    # Generate computer's choice
    computer_choice = random.choice(choices).lower()

    # Compare choices and determine winner
    winner = None

    if player_choice == computer_choice:
        winner = "Tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            winner = "Computer"
        else:
            winner = "Player"
    elif player_choice == "paper":
        if computer_choice == "scissors":
            winner = "Computer"
        else:
            winner = "Player"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            winner = "Computer"
        else:
            winner = "Player"
    else:
        winner = "Invalid choice"

    # Display results
    if winner == "Tie":
        print(f"It's a tie! Both chose {player_choice}.")
    else:
        print(f"{winner.capitalize()} wins! {player_choice.upper()} vs. {computer_choice.upper()}.")

    # Play again option
    play_again = input("Play again? (y/n): ").lower()

print("Thanks for playing!")
