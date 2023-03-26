fruits = ["Apple", "Pear", "Mango"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# <--------------------------Average Height-------------------------->

students_height = input("Input a list of students height. ").split()

sum_of_height = 0
length = 0
for height in students_height:
    length += 1
    sum_of_height += int(height)

aearage_height = round(sum_of_height / length)
print(aearage_height)

# <--------------------------Height Score-------------------------->
student_scores = input("Enter a list of students scores\n").split()

for n in  range(0, len(student_scores)) :
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for score in student_scores:
    if max_score < score:
        max_score = score
print(f"The highest score in the class room {max_score}")

# <--------------------------Sum of 1-100-------------------------->
sum_of_100 = 0
for n in range(1, 101):
    sum_of_100 += n
print(sum_of_100)

# <--------------------------Sum of even number-------------------------->
sum_of_even_number = 0

for n in range(1, 101):
    if n % 2 == 0:
        sum_of_even_number += n
# Alternative--------------->
for n in range(2, 101, 2):
   sum_of_even_number += n
print(sum_of_even_number)

# <--------------------------FizzBuzz game-------------------------->
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    elif num % 3 == 0:
        num = "Fizz"
    elif num % 5 == 0:
        num = "Buzz"
    print(num)

# <--------------------------final: PyPassword generator-------------------------->
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

normal_password = []
for letter in range(nr_letters):
    # letters[random.randint(0, 25)]
    normal_password += random.choice(letters)

for number in range(nr_numbers):
    # numbers[random.randint(0, 9)]
    normal_password += random.choice(numbers)

for symbol in range(nr_symbols):
    #  symbols[random.randint(0, 8)]
    normal_password += random.choice(symbols)

# hard_password = "".join(random.sample(normal_password, len(normal_password)))
random.shuffle(normal_password)

hard_password = ""

for pass_char in normal_password:
    hard_password += pass_char
print(f"You password is {hard_password}")
