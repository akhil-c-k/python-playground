import random

namen = input("Enter your name: ")
print(f"Hello {namen}, welcome to the Guess the Character game!")

words = ['rainbow', 'computer', 'science', 'programming',
   'python', 'mathematics', 'player', 'condition',
   'reverse', 'water', 'board', 'geeks']


word = random.choice(words)
print("Guess the characters")

guessess = ''
turns = 12

while turns > 0:
  failed = 0
  for char in  word:
    if char in guessess:
      print(char, end=" ")
    else:
      print("_", end=" ")
      failed += 1
  if failed == 0:
    print("\nYou Win")
    print(f"The word is: {word}")
    break

  print()
  guess = input("guess a character:")
  guessess += guess
  if guess not in word:
    turns -= 1
    print("Wrong")
    print(f"You have {turns} more guesses")
    if turns == 0:
      print("You Loose")

      
  