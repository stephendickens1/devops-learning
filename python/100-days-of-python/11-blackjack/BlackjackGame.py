# Deal both user and computer a starting hand of 2 random card values.

# HOW TO: Create a deck of 52. Can just be a list, but then what's the value of the card?
# A dictionary that looks like this:
import random
import time

deck_list = {
    1: ["1 of Spades", "1 of Hearts", "1 of Clubs", "1 of Diamonds"],
    2: ["2 of Spades", "2 of Hearts", "2 of Clubs", "2 of Diamonds"],
    3: ["3 of Spades", "3 of Hearts", "3 of Clubs", "3 of Diamonds"],
    4: ["4 of Spades", "4 of Hearts", "4 of Clubs", "4 of Diamonds"],
    5: ["5 of Spades", "5 of Hearts", "5 of Clubs", "5 of Diamonds"],
    6: ["6 of Spades", "6 of Hearts", "6 of Clubs", "6 of Diamonds"],
    7: ["7 of Spades", "7 of Hearts", "7 of Clubs", "7 of Diamonds"],
    8: ["8 of Spades", "8 of Hearts", "8 of Clubs", "8 of Diamonds"],
    9: ["9 of Spades", "9 of Hearts", "9 of Clubs", "9 of Diamonds"],
    10: ["10 of Spades", "10 of Hearts", "10 of Clubs", "10 of Diamonds", "Jack of Spades", "Jack of Hearts", "Jack of Clubs", "Jack of Diamonds", "Queen of Spades", "Queen of Hearts", "Queen of Clubs", "Queen of Diamonds", "King of Spades", "King of Hearts", "King of Clubs", "King of Diamonds"],
    11: ["Ace of Spades", "Ace of Hearts", "Ace of Clubs", "Ace of Diamonds"],
}

drawn_cards = []

house_cards = []
house_score = 0

player_cards = []
player_score = 0

def card_deal():
    random_key = random.choice(list(deck_list.keys()))
    random_set = deck_list[random_key]
    random_card = random.choice(random_set)
    if random_card in drawn_cards and len(drawn_cards) < 52:
        card_deal()
    elif len(drawn_cards) >= 52:
        print("You've drawn the entire deck")
    else:
        drawn_cards.append(random_card)

def house_initial_deal():
    card_deal()
    house_cards.append(drawn_cards[-1])
    card_deal()
    house_cards.append(drawn_cards[-1])
    print(f"House draws TWO CARDS. One is the {house_cards[-1].upper()}!")

def player_initial_cards():
    card_deal()
    player_cards.append(drawn_cards[-1])
    card_deal()
    player_cards.append(drawn_cards[-1])
    print(f"Your cards are {player_cards[0].upper} and {player_cards[1].upper}")


house_initial_deal()
print("Dealing your cards...")
time.sleep(2)
player_initial_cards()
print(player_cards)



should_continue = True

while should_continue == True:
    card_deal()
    deal_again = input("Another card deal? Yes or no: ").lower()
    if deal_again != "yes" and deal_again != "y":
        should_continue = False




print("Thanks for playing")
print(deck_list[10][2])

# Today we make it so that the computer draws two cards, announces one of them to the player.




# We're going to want the game to select a card randomly then look up the key. So because 10
# is so long the look up has to be rand len of the 10
# Detect when computer or user has a blackjack. (Ace + 10 value card).

# If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).

# Calculate the user's and computer's scores based on their card values.

# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.

# Reveal computer's first card to the user.

# Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.

# Ask the user if they want to get another card.

# Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.

# Compare user and computer scores and see if it's a win, loss, or draw.

# Print out the player's and computer's final hand and their scores at the end of the game.

# After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.