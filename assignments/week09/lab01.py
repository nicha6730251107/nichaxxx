"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

def guessing_game():
    print("=== SIMPLE GUESSING GAME ===")
    print("Guess my number between 1 and 20!")
    
    secret_number = random.randint(1, 20)
    max_attempts = 6

    for attempt in range(1, max_attempts + 1):
        while True:
            guess_input = input(f"\nAttempt {attempt}/{max_attempts} - Enter your guess: ")
            if guess_input.isdigit():
                guess = int(guess_input)
                if 1 <= guess <= 20:
                    break
                else:
                    print("Please enter a number between 1 and 20.")
            else:
                print("Invalid input! Please enter a numeric value.")

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You won in {attempt} attempts!")
            return

    print(f"\nSorry, you've used all your attempts. The number was: {secret_number}")

guessing_game()
