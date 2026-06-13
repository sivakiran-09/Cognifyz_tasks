import random

secret_number = random.randint(1, 100)
attempts = 7

print("Welcome to Number Guessing Game! 😉")
print("You have", attempts, "attempts to guess the secret number between 1 and 100. Good luck buddy! 😇")

for i in range(attempts):
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == secret_number:
        print("Wow! You are a genius! You guessed the number correctly! 🥳")
        break

    elif guess < secret_number:
        print("Too Low! Try a higher number! 🥲")

    else:
        print("Too High! Try a lower number! 🥲")

    print("You have", attempts - (i + 1), "attempts left.")

else:
    print("Sorry, that's not the correct number. Better luck next time! 😔")
    print("The secret number was:", secret_number)