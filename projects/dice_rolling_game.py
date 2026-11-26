import random


while True:   # ask for roll dice
  choice = input('Roll the dice? (y/n): ').lower()
  # if user enters y
  if choice == 'y':
      # get he random numbers
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'({die1}, {die2})')
  # if user enters y
  elif choice == 'n':
      print('Thanks for playing......')
      break
  else:
      print('Invalid choice!')



