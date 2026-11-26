import random

# generate a random number
guess_number=random.randint(1,100)
# loop
while True:
  try:
    # aske user to guss the number
    user_number=int(input("Enter number for guess: "))
    # if number < guess
    #    print too low
    if user_number < guess_number:
        print(f"Your user number: {user_number} to low from guess number: {guess_number}")
    # if number > guess
    #    print to high
    elif user_number > guess_number:
        print(f"Your user number: {user_number} to high from guess number: {guess_number}")
    # else
    #     print done
    else:
        print("Done....")
        break
 # if not valid
 # print error
  except ValueError:
    print("Please enter a valid number")







# # ---------------------------------------------------------------------
# import random
#
# def guess(x):
#     random_number=random.randint(1,x)
#     guess=0
#     while guess != random_number:
#         guess=int(input(f"Guess a number between 1 and {x}:"))
#         if guess < random_number:
#             print("sorry guss again : too low")
#         elif guess > random_number:
#             print("sorry guess again : too high")
#     print(f"congrats you have guessed number {random_number} correctly ")
# # guess(10)
#
# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low  # could also be high b/c low = high
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#
#     print(f'Yay! The computer guessed your number, {guess}, correctly!')
#
# guess(10)

