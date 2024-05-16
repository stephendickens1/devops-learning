print("Welcome to the Tip Calculator!")

subtotal = float(input("What was the total bill please?\n"))
people = int(input("And how many people are splitting the bill?\n"))
tip = float(input("Finally, what percent tip would you like to give here?\n"))
total = round(subtotal + subtotal * (tip/100), 2)

def calculation():
  return round(total / people, 2)
  

print(f"A bill of {subtotal} with a {tip} tip will mean {calculation()} to be paid by each of the {people} people")
