############### Blackjack Project #####################
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def sum_of_arr(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while start_game == "y":
    user_card = [random.choice(cards), random.choice(cards)]
    computer_card = [random.choice(cards), random.choice(cards)]
    print(f"    Your cards: {user_card}, current score: {sum_of_arr(user_card)}")
    print(f"    Computer's first card: {computer_card[0]}")

    while sum_of_arr(computer_card) <= 17:
        computer_card.append(random.choice(cards))

    ADD_CARD = input(f"Type 'y' to get another card, type 'n' to pass:")

    while ADD_CARD == "y":
        user_card.append(random.choice(cards))
        print(f"    Your cards: {user_card}, current score: {sum_of_arr(user_card)}")
        print(f"    Computer's first card: {computer_card[0]}")
        if sum_of_arr(user_card) > 21:
            while sum_of_arr(computer_card) > 21:
                computer_card.pop()
            ADD_CARD = "n"
        else:
            ADD_CARD = input(f"Type 'y' to get another card, type 'n' to pass:")

    print(f"    Your final hand: {user_card}, final score: {sum_of_arr(user_card)}")
    print(f"    Computer's final hand: {computer_card}, final score: {sum_of_arr(computer_card)}")
    if sum_of_arr(user_card) > 21:
        print("You went over. You lose 😭")
    elif sum_of_arr(computer_card) > 21:
        print("Opponent went over. You win 😁")
    elif sum_of_arr(user_card) > sum_of_arr(computer_card):
        print("Opponent went over. You win 😁")
    elif sum_of_arr(computer_card) > sum_of_arr(user_card):
        print("Opponent went over. You win 😁")
    else:
        print("Match draw 😉")
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
