"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""
import random

def enhanced_guessing_game():
    print("=== Enhanced GUESSING GAME ===")
    print("Guess my number between 1 and 100!")
    print("You have unlimited attempts.\n")

    secret_number = random.randint(1, 100)
    attempt = 0
    wrong_guesses = 0

    while True:
        guess_input = input(f"Attempt {attempt + 1} - Enter your guess: ")

        if not guess_input.isdigit():
            print("Invalid input! Please enter a numeric value.")
            continue

        guess = int(guess_input)

        if not 1 <= guess <= 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempt += 1

        if guess == secret_number:
            print(f"Congratulations! You won in {attempt} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        wrong_guesses += 1

        if wrong_guesses >= 3 and wrong_guesses < 5:
            parity = "even" if secret_number % 2 == 0 else "odd"
            print(f"HINT: The number is {parity}")
        elif wrong_guesses >= 5 and wrong_guesses < 7:
            hints = []
            if secret_number % 3 == 0:
                hints.append("divisible by 3")
            if secret_number % 5 == 0:
                hints.append("divisible by 5")
            if hints:
                print("HINT: The number is " + " and ".join(hints))
            else:
                print("HINT: The number is NOT divisible by 3 or 5")
        elif wrong_guesses >= 7 and wrong_guesses < 10:
            min_range = max(1, secret_number - 12)
            max_range = min(100, secret_number + 12)
            print(f"HINT: The number is between {min_range} and {max_range}")
        elif wrong_guesses >= 10:
            first_digit = str(secret_number)[0]
            print(f"HINT: The first digit of the number is {first_digit}")

enhanced_guessing_game()
