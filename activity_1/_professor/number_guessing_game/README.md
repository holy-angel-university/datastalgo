# Number Guessing Game

This Python script implements a simple number guessing game where the player tries to guess a randomly generated number between 1 and 100. The game offers three difficulty levels, each with a different number of attempts. The player's score decreases with each attempt, and hints are provided every 5 attempts.

## Functions

`get_valid_guess()`

- This function prompts the user to enter a guess and validates the input. It ensures that the guess is an integer between 1 and 100.
- Returns `guess` (int): A valid integer between 1 and 100.

`choose_difficulty()`

- This function allows the user to choose a difficulty level for the game. The difficulty levels determine the number of attempts the player has to guess the number.
- Returns `max_attempts` (int): The maximum number of attempts based on the chosen difficulty level (100 for Easy, 50 for Medium, 25 for Hard).

`number_guessing_game()`

- This is the main function that runs the number guessing game. It sets up the game, handles the game loop, and provides feedback to the player.

## Game Flow

1. **Welcome Message**: The game starts with a welcome message.

2. **Choose Difficulty**: The player is prompted to choose a difficulty level, which determines the number of attempts they have.

3. **Generate Secret Number**: A random number between 1 and 100 is generated as the secret number.

4. **Main Game Loop**:

   - The player is prompted to enter a guess.
   - The guess is validated and compared to the secret number.
   - Feedback is provided based on the guess (too low, too high, or correct).
   - The player's score decreases with each attempt.
   - Hints are provided every 5 attempts.
   - The game continues until the player either guesses the number correctly or runs out of attempts.

5. **End Game**:

   - If the player guesses the number correctly, a congratulatory message is displayed along with the final score.
   - If the player runs out of attempts, a message reveals the secret number.
   - The player is asked if they want to play again.

## Example Output

```shell
Welcome to the Number Guessing Game!
Choose a difficulty level:
1. Easy (100 attempts)
2. Medium (50 attempts)
3. Hard (25 attempts)
Enter the number of your choice (1-3): 2
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too high! Try again.
You have 49 attempts left.
Enter your guess: 25
Too low! Try again.
You have 48 attempts left.
...
Congratulations! You've guessed the number 42 correctly in 10 attempts!
Your score is: 90
Do you want to play again? (yes/no): no
Thanks for playing! Goodbye.
```

## Running the Game

To run the number guessing game, execute the script. The game will start automatically if the script is run directly:

```shell
python main.py
```