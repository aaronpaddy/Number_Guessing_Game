# Number Guessing Game

This is a simple **Number Guessing Game** implemented in Python. The computer randomly selects a number between 1 and 100, and the player has to guess it. After each guess, the program provides feedback on whether the guess is too high or too low. The game also limits the number of attempts to 5, after which the correct number is revealed if the player doesn't guess it.

## Features

- The player has **5 attempts** to guess the correct number.
- After each guess, the program provides feedback:
  - "Too low!" if the guess is lower than the secret number.
  - "Too high!" if the guess is higher than the secret number.
  - "Congratulations!" when the correct number is guessed.
- The number of **remaining attempts** is displayed after each guess.
- If the player runs out of attempts, the correct number is revealed.
- After the game ends, the player is asked if they want to play again.

## How to Play

1. When the game starts, the program randomly selects a number between **1 and 100**.
2. The player is prompted to enter a guess.
3. The program provides feedback on whether the guess is too low or too high.
4. The player has **5 attempts** to guess the number correctly.
5. If the player fails to guess the number within the 10 attempts, the correct number is displayed.
6. After the game ends, the player can choose to play again or exit.

## Requirements

- Python 3.x

## How to Run the Game

1. Clone or download the repository to your local machine.
2. Navigate to the project folder.
3. Run the following command in your terminal to start the game:

   ```bash
   python number_guessing.py
   ```

4. Follow the on-screen instructions to play the game.


## Customization

- You can change the number of allowed attempts by modifying the `max_attempts` variable in the code.
- You can adjust the range of the random number by changing the `random.randint(1, 100)` part of the code.
