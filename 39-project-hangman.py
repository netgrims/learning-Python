import os, time, random

listOfWords = ["stronghold", "wellspring", "thumbscrew", "subway", "galaxy", "buffalo"]
print("""
                                               
    /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  
   / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  / __  / (_| | | | | (_| | | | | | | (_| | | | |
  \/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     |___/                       
  """)
menu = input("Do you want to let the computer choose a word for you?\n> ")
if menu == "yes":
  wordChosen = random.choice(listOfWords)
else:
  wordChosen = input("Enter your word here: ")

os.system("clear")

# Making a list of letters in the correct word (removing doubles)
wordChosenLetters = []
for correctLetter in wordChosen:
  if correctLetter not in wordChosenLetters:
    wordChosenLetters.append(correctLetter)

guessedLetters = []

# Guess counts
wrongGuesses = 0
rightGuesses = 0

while True:
  print("""
                                               
    /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  
   / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  / __  / (_| | | | | (_| | | | | | | (_| | | | |
  \/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     |___/                       
  """)
  print()
  if wrongGuesses == 0:
    print("""
                  .___.
                     \|
                      |
                      |
                      |
                      |
                =========
    """)
  elif wrongGuesses == 1:
    print("""
                  .___.
                  |  \|
                      |
                      |
                      |
                      |
                =========
    """)
  elif wrongGuesses == 2:
    print("""
                  .___.
                  |  \|
                  O   |
                      |
                      |
                      |
                =========
    """)
  elif wrongGuesses == 3:
    print("""
                  .___.
                  |  \|
                  O   |
                  |   |
                      |
                      |
                =========
    """)
  elif wrongGuesses == 4:
    print("""
                  .___.
                  |  \|
                  O   |
                 /|   |
                      |
                      |
                =========
    """)
  elif wrongGuesses == 5:
    print("""
                  .___.
                  |  \|
                  O   |
                 /|\  |
                      |
                      |
                =========
    """)
  elif wrongGuesses == 6:
    print("""
                  .___.
                  |  \|
                  O   |
                 /|\  |
                 /    |
                      |
                =========
    """)
  elif wrongGuesses == 7:
    print("""
                  .___.
                  |  \|
                  O   |
                 /|\  |
                 / \  |
                      |
                =========
  """)
  print()
  print("Your word: ",end="")
  for letter in wordChosen:
    if letter in guessedLetters:
      print(letter, end='')
    if letter not in guessedLetters:
      print("_", end="")
  print()
  print()
  if wrongGuesses == 7: # Player dead
    print("You're dead! Game over.")
    print()
    time.sleep(1.5)
    print(f"The correct word was {wordChosen}")
    print()
    break
  elif rightGuesses == len(wordChosenLetters): # Player wins
    time.sleep(1.5)
    print(f"You won! You had {7-wrongGuesses} lives left.")
    print()
    break
  letterGuess = input("Choose a letter: ") # Input
  if letterGuess in guessedLetters:
    print("You already guessed that one! Try again.")
  else:
    guessedLetters.append(letterGuess)
    if letterGuess in wordChosen:
      print()
      print("Correct!")
      rightGuesses += 1
    elif letterGuess not in wordChosen:
      print()
      print("Nope, not in there.")
      wrongGuesses += 1
  print()
  time.sleep(2)
  os.system("clear")
