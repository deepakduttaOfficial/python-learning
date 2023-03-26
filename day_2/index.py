total_bil = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_split = int(input("How many people to split the bill? "))

each_people_pay = (total_bil + (total_bil * tip/100)) / people_split

print(f"Each person should pay { round(each_people_pay, 1)}")

# another one
print(12323_3434)
print(True)
print(False)

print(float('10') + 56)
take_int_input = input("Write your number \n")
first_int_input = int(take_int_input[0])
second_int_input = int(take_int_input[1])

total = first_int_input + second_int_input

print("Sum of this number is = " + str(total))

# Another code ------------->
print(3 *( 3 + 3) / 3 - 3)

# Another Challenge -----------------> BMI calculator
height = float(input("What is your hight? m: "))
weight = float(input("What is your weight? kg: "))

BMI = weight / (height ** 2)


# Another one ---------->
print(10 // 3)
print(10 // 2)
score = 1
score +=1
score -=1
score *=1
score /=1
score //=1
print(score)

# Another one ---------- "f" string
name = "Deepak"
score = 12
print(f"My name is {name}, and my score is {score}")

# Another Challenge ----------------->
age = input("What is your correct age? ")
remaining_years = 90 - int(age)
remaining_days = remaining_years * 365
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52

print(f"You have {remaining_days}, {remaining_weeks}, and {remaining_months} left")
