import random

def difficulty_selection():
    life_checker = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if life_checker == 'hard':
        return 5
    elif life_checker == 'easy':
        return 10
    else:
        print("I'm sorry, I didn't recognise that option.")
        return difficulty_selection()

def gameplay():
    number_to_guess = random.randint(1, 100)
    lives = difficulty_selection()
    winner = False
    while lives > 0 and winner == False:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            winner = True
        elif guess > number_to_guess:
            print("Too high. Guess again")
            lives -= 1
        else:
            print("Too low. Guess again")
            lives -= 1

    if winner == True:
        print(f"You guessed {number_to_guess} correctly. YOU WIN!")
    else:
        print(f"The number was {number_to_guess}. Unlucky mate.")

    again = input("Do you want to play again? Type 'yes' or 'no': ").lower()

    if again == "yes":
        gameplay()

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

gameplay()

