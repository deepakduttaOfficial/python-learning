# <------------------ return function ---------------------->

def formate_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_str = formate_name("deepak", "sarah")
print(formatted_str)

# <----------------- Leap year challenge ------------------------>
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year , month):
  year_input = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if year_input == True:
    if month == 2:
      return 29
    else:
      return month_days[month - 1]
  elif year_input == False:
    return month_days[month - 1 ]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# <------------------ calculator ------------>
import os
from art import logo
print(logo)
def calculate(n1, n2, operator):
    if operator == "+":
        return n1 + n2

    elif operator == "-":
        return n1 - n2

    elif operator == "*":
        return n1 * n2

    elif operator == "/":
        return n1 / n2

n1 = int(input("What's the first number?: "))
operator = input("+\n-\n*\n/\nPick an operation: ")
n2 = int(input("What's the second number?: "))


def calculator(n1, n2, operator):
    calculate_result = calculate(n1, n2, operator)
    print(f"{n1} {operator} {n2} = {calculate_result}")
    is_continue = input("Type 'y' to continue calculating with 4.0, or type 'n' to start a new calculation: ")
    CONTINUE = True
    while CONTINUE:
        if is_continue == 'y':
            operator = input("Pick an operation: ")
            n2 = int(input("What's the second number?: "))
            calculate_result = calculate(calculate_result, n2, operator)
            print(f"{calculate_result} {operator} {n2} = {calculate_result}")
            CONTINUE = True
        else:
            os.system('cls')
            CONTINUE = False
calculator(n1, n2, operator)