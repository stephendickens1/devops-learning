def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

operator_dict = {
    "+": addition,
    "-": subtraction, 
    "*": multiplication,
    "/": division
}

a = int(input("What's the first number?: "))


for operator in operator_dict:
    print(operator)

operator_selection = input("Pick an operation from the line above: ")

b = int(input("What's the second number?: "))

firstanswer = operator_dict[operator_selection](a, b)

print(f"{a} {operator_selection} {b} = {firstanswer}")

again = True

while again == True:
    for operator in operator_dict:
        print(operator)

    operator_selection = input("Pick an operation from the line above: ")
    c = int(input("What's the next number?: "))

    secondanswer = operator_dict[operator_selection](firstanswer, c)

    print(f"{firstanswer} {operator_selection} {c} = {secondanswer}")

    goagain = input("Would you like to perform another function? Type Yes or No: " ).lower()
    if goagain != "yes" and goagain != "y":
        again = False