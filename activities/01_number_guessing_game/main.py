import random


def get_valid_guess():
    # :: Validate user input for the guess
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def choose_difficulty():
    # :: Allow the user to choose a difficulty level
    while True:
        print("Choose a difficulty level:")
        print("1. Easy (100 attempts)")
        print("2. Medium (50 attempts)")
        print("3. Hard (25 attempts)")
        try:
            choice = int(input("Enter the number of your choice (1-3): "))
            if choice == 1:
                return 100
            elif choice == 2:
                return 50
            elif choice == 3:
                return 25
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


def number_guessing_game():
    # :: Welcome message and set up the game
    print("Welcome to the Number Guessing Game!")
    max_attempts = choose_difficulty()
    secret_number = random.randint(1, 100)
    attempts = 0
    # :: Initial score
    score = 100

    print("I'm thinking of a number between 1 and 100.")

    # :: Main game loop
    while attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1
        # :: Deduct 1 point for each attempt
        score -= 1

        # :: Compare the user's guess to the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # :: Provide feedback (correct guess)
            print(
                f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!"
            )
            print(f"Your score is: {score}")
            break

        # :: Display remaining attempts
        print(f"You have {max_attempts - attempts} attempts left.")

        # :: Provide hints every 5 attempts
        if attempts % 5 == 0:
            if secret_number % 2 == 0:
                print("Hint: The secret number is even.")
            else:
                print("Hint: The secret number is odd.")

    # :: Handle the case where the user runs out of attempts
    else:
        print(
            f"Sorry, you've run out of attempts. The secret number was {secret_number}."
        )

    # :: Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye.")


# :: Start the game
if __name__ == "__main__":
    number_guessing_game()
