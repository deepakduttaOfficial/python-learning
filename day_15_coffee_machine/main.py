from resource import MENU, resources
from math import ceil

# Current resources
current_water, current_milk, current_coffee = resources.values()

IS_FINISHED_RESOURCE = ""
TOTAL_EARN_MONEY = 0

while True:
    # Taking input from user 
    coffee_name = input("   What would you like? (espresso/latte/cappuccino): ")
    if coffee_name == "report":
        print(f"Water:{current_water}\nMilk:{current_milk}\nCoffee:{current_coffee}\nMoney:{TOTAL_EARN_MONEY}")
    else:
        # Coffee requirement
        ingredients, cost = MENU[coffee_name].values()

        # Destructing the ingredients
        ingredient_water, ingredient_milk, ingredient_coffee = ingredients.get('water', 0), ingredients.get('milk', 0), ingredients.get('coffee', 0)

        if current_water < ingredient_water:
            IS_FINISHED_RESOURCE = "water"
        elif current_milk < ingredient_milk:
            IS_FINISHED_RESOURCE = "milk"
        elif current_coffee < ingredient_coffee:
            IS_FINISHED_RESOURCE = "coffee"

        if IS_FINISHED_RESOURCE != "":
            print(f"    Sorry there is not enough {IS_FINISHED_RESOURCE}.")
        else:
            print("Please insert coins.")
            quarters_to_cent = int(input("how many quarters?: ")) * 25
            dimes_to_cent = int(input("how many dimes?: ")) * 10
            nickles_to_cent = int(input("how many nickles?: ")) * 5
            pennies_to_cent = int(input("how many pennies?: "))
            user_money = (quarters_to_cent + dimes_to_cent + nickles_to_cent + pennies_to_cent) / 100

            if user_money < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${round(user_money - cost, 2)} in change\nHere is your cappuccino ☕️. Enjoy!")
                current_water -= ingredient_water
                current_milk -= ingredient_milk
                current_coffee -= ingredient_coffee
                TOTAL_EARN_MONEY += cost