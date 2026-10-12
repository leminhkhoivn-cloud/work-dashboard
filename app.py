import random

def run_app():
    print("Welcome to the Number Guessing App! 🎮")
    print("I'm thinking of a number between 1 and 10.")
    
    secret_number = random.randint(1, 10)
    attempts = 3
    
    while attempts > 0:
        guess = input(f"\nYou have {attempts} guesses left. Enter your guess: ")
        
        # Check if the user actually entered a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
            
        guess = int(guess)
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed it! The number was {secret_number}.")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
            
        attempts -= 1
        
    print(f"\nGame over! The secret number was {secret_number}.")

# This ensures the app runs when you execute the file
if __name__ == "__main__":
    run_app()
    