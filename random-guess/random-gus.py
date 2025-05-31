import random

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

print(f"\n You have 7 chances to guess the number correctly between {low} and {high}. Lets Start\n")

num = random.randint(low, high)
ch = 7
gc = 0 

while gc < ch :
  gc += 1
  guess = int(input(f"Guess {gc}: "))
  if guess == num:
    print(f"Congratulations! You guessed the number {num} correctly in {gc} attempts.")
    break  
  elif gc >= ch and guess != num:
    print(f"Sorry, you have used all your chances. The number was {num}.")
    break
  elif guess > num:
    print("Your guess is too high. Try again.")

  elif guess < num:
    print("Your guess is too low. Try again.")


