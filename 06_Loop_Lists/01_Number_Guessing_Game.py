# Number Guessing Game
import random
def generate_random_number(min, max):
    return random.randint(min, max)

def play_game(secret_number, max_attempt=10):
    attempts = 0
    guessed_number = []

    while attempts < max_attempt:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempt} - Enter your guess: "))
        guessed_number.append(guess)
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            print(f" your guess: {guessed_number}")
            return True
        elif guess <= secret_number:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")
    print(f"X. GameOver! the number was {secret_number}")
    print(f"your guess: {guessed_number}")
    return False

if __name__ == "__main__":
    print("---- Number Guessing Game ----")
    print("Guess the number between 1 and 100")
    secret = generate_random_number(1, 100)
    play_game(secret)