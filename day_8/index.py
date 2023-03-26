# <----------------- function learning, single input ------------------>
# def greet(name):
#     print(f"Hello, {name}")
#     print(f"What's app {name}?")
#     print("Isn't the weather nice Today?")

# greet("Deepak")
# <---------------------------------------------------->

# <----------------- function learning, two input ------------------>

# def greet_with(name, location):
#     print(f"Welcome {name} in {location}")

# greet_with("Deepak", "India")
# <---------------------------------------------------->

# <----------------- another way to pass argument ------------------>
# def greet_with(name, location):
#     print(f"Welcome {name} in {location}")

# greet_with( location="India", name="Deepak")


# <----------------- code challenge ------------------>
from math import ceil
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
    number_of_cans = ceil((height * width)/ cover)
    print(f"You'll need {number_of_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)


