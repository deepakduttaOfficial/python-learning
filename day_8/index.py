# <----------------- function learning, single input ------------------>
def greet(name):
    print(f"Hello, {name}")
    print(f"What's app {name}?")
    print("Isn't the weather nice Today?")

greet("Deepak")
# <---------------------------------------------------->

# <----------------- function learning, two input ------------------>

def greet_with(name, location):
    print(f"Welcome {name} in {location}")

greet_with("Deepak", "India")
# <---------------------------------------------------->

# <----------------- another way to pass argument ------------------>
def greet_with(name, location):
    print(f"Welcome {name} in {location}")

greet_with( location="India", name="Deepak")


#<----------------- code challenge ------------------>
from math import ceil
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
    number_of_cans = ceil((height * width)/ cover)
    print(f"You'll need {number_of_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)

#<----------------- code challenge(prime number checker) ------------------>
n = int(input("Check this number: "))

def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


prime_checker(number = n)

#<----------------- code challenge(caesar-cipher) ------------------>
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

CONTINUE = True
while CONTINUE:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(text, shift):
        if direction == "encode":
            encrypt = ""
            for n in range(len(text)):
                letter = text[n]
                index_number = alphabet.index(letter)
                decode_letter = alphabet[index_number + shift]
                encrypt += decode_letter
            print("Here's the encoded result: "+ encrypt)
        else:
            decrypt = ""
            for n in range(len(text)):
                letter = text[n]
                index_number = alphabet.index(letter)
                decode_letter = alphabet[index_number - shift]
                decrypt += decode_letter
            print("Here's the decoded result: " + decrypt)

        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") 
        
        if again == "yes":
            CONTINUE = True
        else:
            CONTINUE = False
        
encrypt(text, shift)