import random

import my_module

random_int = random.randint(1, 10)

print(random_int)
print(my_module.pi)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"You love score is {love_score}")

# <------------------------------------------------------->
random_num = random.randint(1, 2)
if random_num == 1:
    print("HEAD")
else:
    print("TAIL")

# <-----------------------List-------------------------------->

states_of_india = ["West Bengal", "Uttar Pradesh", "Gujrat", "Bihar"]
print(states_of_india[0])
states_of_india.append("DeepakLand")
print(states_of_india)

# <-----------------------List-challenge-------------------------------->
names = input("Give me Everybody's names, seperated by a comma and space\n")
names_list = names.split(", ")

total_person = len(names_list)

random_person = random.randint(0, total_person-1)
# random_person = random.choice(names_list)

print(f"{names_list[random_person]} is going the buy the meal today")

# <-----------------------Treasure-hunter-------------------------------->
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
print(f"{row1}\n{row2}\n{row3}")

treasure_location = input("Where do you want to put the treasure\n")

first_point = int(treasure_location[0]) - 1
second_point = int(treasure_location[1]) - 1

combine_box = [row1, row2, row3]
hiding_treasure = combine_box[second_point]
hiding_treasure[first_point] = "X"

print(f"{combine_box[0]}\n{combine_box[1]}\n{combine_box[2]}")

# <-----------------------rock_paper_scissor-hunter-------------------------------->

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''  

user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choise = random.randint(0, 2)
rock_paper_scissors = [rock, paper, scissors]

print(f"You choose\n {rock_paper_scissors[user_choise]}")
print(f"Computer Choise\n{rock_paper_scissors[computer_choise]}")



if user_choise == computer_choise:
    print("Draw")
elif user_choise == 0 and computer_choise == 1:
    print("You lose")
elif user_choise == 1 and computer_choise == 0:
    print("You win")
elif user_choise == 1 and computer_choise == 2:
    print("You lose")
elif user_choise == 2 and computer_choise == 1:
    print("You win")
elif user_choise == 0 and computer_choise == 2:
    print("You win")
elif user_choise == 2 and computer_choise == 0:
    print("You lose")


