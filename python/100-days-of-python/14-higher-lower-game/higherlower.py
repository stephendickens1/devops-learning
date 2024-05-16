import random
from data import data
from art import logo, vs

DATA_LEN = len(data)

def create_celeb(letter):
    rand_celeb = data[random.randint(0, DATA_LEN-1)]
    name = rand_celeb['name']
    description = rand_celeb['description']
    country = rand_celeb['country']
    follower_count = rand_celeb['follower_count']
    return assign_to_option(letter, name, description, country, follower_count)

def assign_to_option(letter, name, description, country, follower_count):
    lista = []
    listb = []
    if letter == "A":
        print(logo)
        print(f"Compare {letter}: {name}, a {description}, from {country}")
        lista.extend((name, description, country, follower_count))
        return lista
    elif letter == "B":
        print(vs)
        print(f"Against {letter}: {name}, a {description}, from {country}")
        listb.extend((name, description, country, follower_count))
        return listb
        
def assess_guess(lista, listb):
    while True:
        guess = input("Who has more followers? Type 'A' or 'B':").lower()
        if guess == "a" and lista[3] > listb[3]:
            return True
        elif guess == "b" and listb[3] > lista[3]:
            return True
        elif guess == "a" and lista[3] < listb[3]:
            return False
        elif guess == "b" and listb[3] < lista[3]:
            return False
        else:
            print("I don't recognise that selection.")
        print(f"lista {lista[3]}, listb {listb[3]}")
    

def game():
    lista = create_celeb(letter = "A")
    listb = create_celeb(letter = "B")

    score = 0
    correctguess = assess_guess(lista, listb)
    while correctguess == True:
        score += 1
        lista = listb
        print(logo)
        print(f"That's right! Current score {score}")
        print(f"Compare A: {lista[0]}, a {lista[1]}, from {lista[2]}")
        listb = create_celeb(letter = "B")
        correctguess = assess_guess(lista, listb)
    
    print(f"That's wrong! Your final score is {score}")
    
game()


    
    
