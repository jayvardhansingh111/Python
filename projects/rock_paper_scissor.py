
# # ask the user to make choice
# # if choice is not valid
# #    print error
# # let the computer to make a choice
# # print choice imoji
# # determine the winner
# # aske the user if they want to continue
# # if not
# #   terminate
#
#
# import  random
#
# choices=('r','p','s')
# emojis={'r':'🪨🪨', 's':'✂️✂️','p':'📜📜'}
#
# while True:
#     # ask the user to make choice
#     user_choice = input("Rock,Paper,Scissor ? (r/s/p):  ").lower()
#     # if choice is not valid
#     #    print error
#     if user_choice not in choices:
#         print('invalid choice...')
#         continue
#     # let the computer to make a choice
#     computer_choice = random.choice(choices)
#     # print choice imoji
#     print(f'You choice: {emojis[user_choice]}..')
#     print(f'Computer choice: {emojis[computer_choice]}..')
#
#     # determine the winner
#     if user_choice == computer_choice:
#         print("Match Draw......")
#     elif (
#             (user_choice == 'r' and computer_choice == 's') or
#             (user_choice == 'p' and computer_choice == 'r') or
#             (user_choice == 's' and computer_choice == 'p')):
#         print("You win")
#     else:
#         print('You lose')
#
#     # aske the user if they want to continue
#     # if not
#     #   terminate
#     should_continue = input('Continue? (y/n): ').lower()
#     if should_continue == 'n':
#         print("Game over..")
#         break





# # ------------------------------------------------------------------------
#
# import random
#
# emojis={'r':'🪨🪨', 's':'✂️✂️','p':'📜📜'}
# choices=tuple(emojis.keys())
#
# # function to get user choice --------------------
# def get_user_choice():
#     while True:
#         # ask the user to make choice
#         user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
#         if user_choice in choices:
#             return user_choice
#         else:
#             print('Invalid choice!')
#
#
# def display_choices(user_choice, computer_choice):
#     print(f'You chose {emojis[user_choice]}')
#     print(f'Computer chose {emojis[computer_choice]}')
#
#
# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         print('Tie!')
#     elif (
#             (user_choice == 'r' and computer_choice == 's') or
#             (user_choice == 's' and computer_choice == 'p') or
#             (user_choice == 'p' and computer_choice == 'r')):
#         print('You win')
#     else:
#         print('You lose')
#
#
# def play_game():
#     while True:
#         user_choice = get_user_choice()
#
#         computer_choice = random.choice(choices)
#
#         display_choices(user_choice, computer_choice)
#
#         determine_winner(user_choice, computer_choice)
#
#         should_continue = input('Continue? (y/n): ').lower()
#         if should_continue == 'n':
#             break
#
#
# play_game()





# ------------------------------------------------------------------------


import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())








