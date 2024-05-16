#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91



llength = len(letters)
letterlist = []

for letter in range(0, nr_letters):
    randletter = random.randint(0, llength - 1)
    letterlist.append(letters[randletter])

nlength = len(numbers)
numberlist = []

for number in range(0, nr_numbers):
  randnumber = random.randint(0, nlength - 1)
  numberlist.append(numbers[randnumber])

slength = len(symbols)
symbolist = []

for s in range(0, nr_symbols):
  randsymbol = random.randint(0, slength - 1)
  symbolist.append(symbols[randsymbol])

password = "".join(letterlist)+"".join(numberlist)+"".join(symbolist)

print(f"Your unshuffled password is {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

originallist = list(password)
shuffledlist = list(password)

random.shuffle(shuffledlist)

shuffledpassword = "".join(shuffledlist)

print(f"Your secure password is {shuffledpassword}")
