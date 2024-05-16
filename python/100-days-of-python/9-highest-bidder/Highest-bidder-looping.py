from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.


# Each persons name needs to be the key, the bid needs to be the value

# At the end of the program we figure out who has made the highest bid.

print(art.logo)

dict_of_bids = {}

more_bidders = True

def add_bid_to_dictionary():
  name = str(input("Enter your name:\n"))
  bid = int(input("Enter your bid:\n"))

  dict_of_bids[name] = bid

def find_highest(bids):
  highest_bidder = ''
  highest_bid = 0
  for bidder in dict_of_bids:
    if dict_of_bids[bidder] > highest_bid:
      highest_bid = dict_of_bids[bidder]
      highest_bidder = bidder
  print(f" The winning bid of {highest_bid} was made by {highest_bidder}! Congratulations!")

while more_bidders == True:
  add_bid_to_dictionary()
  
  question = input("Are we expecting another bidder?\n").lower()

  if question != "yes":
    more_bidders = False
  clear()

find_highest(dict_of_bids)


