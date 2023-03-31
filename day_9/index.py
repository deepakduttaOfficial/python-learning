## <----------------------blind-auction------------------------------>

import os
from art import logo
print(logo)
def auction():
    CONTINUE = True
    list_of_bid = []
    while CONTINUE:
        person_name = input('What is your name: ')
        bid = int(input('What is your bid: '))
        list_of_bid.append({'name': person_name, 'bid': bid})
        is_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
        if is_continue == "yes":
            CONTINUE = True
            os.system('cls')
        else:
            CONTINUE = False

    highest_bid = 0
    highest_bid_person_name = ""

    for item in list_of_bid:
        if highest_bid < item["bid"]:
            highest_bid = item["bid"]
            highest_bid_person_name = item["name"]
        elif highest_bid == item["bid"]:
            highest_bid = highest_bid
            highest_bid_person_name = highest_bid_person_name

    print(f"The winner is {highest_bid_person_name} with a bid of ${highest_bid}")
auction()