 # dice_roller.py
# A tiny Dice Roller Game

import random

def roll_dice():
    """Return a random number between 1 and 6."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Roller Game!")
    while True:
        choice = input("\nDo you want to roll the dice? (y/n): ").strip().lower()
        if choice == 'y':
            print("🎲 You rolled:", roll_dice())
        elif choice == 'n':
            print("Thanks for playing! 🎯")
            break
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
