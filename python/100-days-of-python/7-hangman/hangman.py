import hangman_words
import hangman_art
import random
import os


stages = hangman_art.stages

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(hangman_art.logo)
print("Welcome to Hangman! Enter 'attempts' at any time to show your guesses.")

display = []
lives = 7
guessed_letters = []

def word_select():
  for letter in range(len(chosen_word)):
    display.append("_")

def guessing():
  global lives
  global guessed_letters
  guess = input("Guess a letter: ").lower()
  os.system('clear')
  if guess == "attempts" and (len(guessed_letters)) == 0:
    print("You've not guessed anything yet")
  elif guess == "attempts":
    print("Guesses so far:")
    print(guessed_letters)
  else:
    if guess in chosen_word and not guess in guessed_letters:
      print(f"{guess} is there!")
      guessed_letters.append(guess)
    elif guess not in chosen_word and not guess in guessed_letters:
      print(f"{guess} is not in the word")
      guessed_letters.append(guess)
      lives -= 1
    elif guess in guessed_letters and guess not in chosen_word:
      print(f"You have already guessed {guess}. It wasn't there.")
    elif guess in guessed_letters and guess in chosen_word:
      print(f"You have already guessed {guess}. It was there!")

  print(stages[lives-1])
  
  for nom, letter in enumerate(chosen_word):
    if letter == guess:
      display[nom] = guess
      
  print(display)

# Game starts here

word_select()
print(stages[lives-1])

while "_" in display:
  guessing()
  if lives == 1:
    break

if "_" in display:
  print(f"You've been hung! The word was {chosen_word}")
else:
  print(f"You guessed the word! It was {chosen_word}!")
