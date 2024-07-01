import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess the number!")

    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Prompt the user to enter a guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guessing_game()
