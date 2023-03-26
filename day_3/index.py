height = int(input("What is your height in CM? "))

if (height >= 120):
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride")

value = int(input("What is your number? "))


if value % 2 == 0:
    print("This is a even number")
else:
    print("This is a odd number")

# Another challenge --------------->

height = int(input("Enter you height? "))

if height > 120:
    print("You can ride ")
    age = int(input("Enter you age? "))
    bill = 0
    if age < 12:
        print("Please pay $5")
        bill = 5
    elif age <= 18:
        print("Please pay $7")
        bill = 7
    else:
        print("Please pay $12")
        bill = 12
    wants_photo = input("Do you want a photo token Y or N. ")

    if wants_photo == "Y":
        bill += 3
        print(f"Your total bill including photo token {bill}")
    else:
        print(f"Your total bill including photo token {bill}")
else:
    print("Sorry, You can't ride")

# BMI Calculator 2.0----------------->

height = float(input("What is your hight? m: "))
weight = float(input("What is your weight? kg: "))
BMI = round(weight / (height**2))
if BMI < 18.5:
    print(f"under weight {BMI}")
elif BMI < 25:
    print(f"Normal weight {BMI}")
elif BMI < 30:
    print(f"Over weight {BMI}")
elif BMI < 35:
    print(f"obese {BMI}")
else:
    print(f"clinically obese {BMI}")
print(int(BMI))

# Leap year 2.0----------------->
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    print("1st check pass")
    if year % 100 != 0:
        print("2nd check pass")
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("3rd check failed")
    else:
        print("2nd check failed")
else:
    print("1st check failed")

# Pizza deliveries!
size = input("What size of pizza do you want? S, M or L\n")
add_pepperoni = input("Do you want Pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
price = 0
if size == "S":
    price += 15
    if add_pepperoni == "Y":
        price += 2

elif size == "M":
    price += 20
    if add_pepperoni == "Y":
        price += 3

elif size == "L":
    price += 25
    if add_pepperoni == "Y":
        price += 3

if extra_cheese == "Y":
    price += 1


print(f"Your final bill is: ${price}")

# Love calculator----------->

name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

true_count = 0
love_count = 0


true_count += (name1 + name2).count("t")
true_count += (name1 + name2).count("r")
true_count += (name1 + name2).count("u")
true_count += (name1 + name2).count("e")

love_count += (name1 + name2).count("l")
love_count += (name1 + name2).count("o")
love_count += (name1 + name2).count("v")
love_count += (name1 + name2).count("e")

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


print(f"You score is {score}")


# Treasure land-------------------------------> Challenge

print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Deepak]
*******************************************************************************
'''
)

print("Welcome to Treasure Island, You mission is to find the treasure")

left_right = input("Where you want to go. Left or Right?\n").lower()

if left_right == "left":
    swim_wait = input("Do you wanna swim or wait?\n").lower()
    if swim_wait == "wait":
        if which_door == "red":
            print("Burned by fire. Game Over")
        elif which_door == "yellow":
            print("You win!")
        elif which_door == "blue":
            print("Eated by beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("Attack by trout. Game Over")
else:
    print("Fall into hole. Game Over")
