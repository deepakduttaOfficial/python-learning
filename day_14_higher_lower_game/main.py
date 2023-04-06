from art import logo, vs
from game_data import data
from random import choice
from os import system, name

current_score = 0

def random_item():
    return choice(data)

IS_GAME_OVER = False
choice_a = random_item()
choice_b = random_item()
while not IS_GAME_OVER:
    print(logo)
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}, cheating {choice_a['follower_count']}") 
    print(vs)
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}cheating {choice_b['follower_count']}") 

    response = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice_a['follower_count'] > choice_b['follower_count'] and response == 'a':
        current_score += 1
        choice_a = choice_b
        choice_b = random_item()
        system('cls')
    elif choice_b['follower_count'] > choice_a['follower_count'] and response == "b":
        current_score += 1
        choice_a = choice_b
        choice_b = random_item()
        system('cls')
    else:
        IS_GAME_OVER = True

    if not IS_GAME_OVER:
        print(f"You're right! Current score: {current_score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")