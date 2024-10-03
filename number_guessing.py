import random

def number_guessing_game():
    while True: 
        secret_number = random.randint(1, 100)
        max_attempts = 5
        attempts_left = max_attempts
        guess_count = 0
        
        print("\nWelcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess it correctly.")
        
        while attempts_left > 0:
            guess = int(input(f"Enter your guess (Attempts left: {attempts_left}): "))
            guess_count += 1
            attempts_left -= 1  

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {guess_count} attempts.")
                break 
            if attempts_left == 0:
                print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break  
        
number_guessing_game()
