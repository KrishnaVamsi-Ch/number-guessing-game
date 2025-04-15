import random

def guess_number():
    print("🎲 Welcome to the Number Guessing Game!")
    print("Choose difficulty: easy (1-10), medium (1-50), hard (1-100)")

    level = input("Enter level (easy/medium/hard): ").lower()
    if level == "easy":
        max_num = 10
        attempts = 5
    elif level == "medium":
        max_num = 50
        attempts = 7
    elif level == "hard":
        max_num = 100
        attempts = 10
    else:
        print("Invalid choice. Defaulting to medium.")
        max_num = 50
        attempts = 7

    secret_number = random.randint(1, max_num)

    while attempts > 0:
        try:
            guess = int(input(f"Guess a number between 1 and {max_num}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == secret_number:
            print("🎉 Congratulations! You guessed it right!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print(f"Attempts left: {attempts}\n")

    if attempts == 0:
        print(f"😢 You ran out of attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_number()
