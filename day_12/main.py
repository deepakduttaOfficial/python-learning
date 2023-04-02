import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

print(f"Pssst, the correct answer is {random_number}")

game_difficultly = input("Choose a difficulty. Type 'easy' or 'hard': ")

total_live = 0

if game_difficultly == 'easy':
    total_live = 10
elif game_difficultly == 'hard':
    total_live = 5
else:
    total_live = 0

is_win = False
while total_live > 0 and not is_win:
    print(f"You have {total_live} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    if guess_number == random_number:
        is_win = True
    elif guess_number < random_number:
        print("Too low")
        total_live -= 1
    elif guess_number > random_number:
        print("Too high")
        total_live -= 1
    if not is_win and total_live != 0:
        print("Guess again")
    elif not is_win:
        print(f"You've run out of guesses, you lose")
    elif is_win:
        print(f"You got it! The answer was {random_number}.")

    