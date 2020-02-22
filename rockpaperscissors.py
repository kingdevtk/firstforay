# This is a rock, paper, scissors game.

import random
import sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of wins, losses, and ties.

wins = 0
losses = 0
ties = 0

while True:  # the main game loop
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    while True:  # the input player loop
     print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
     player_move = input()
     if player_move == 'q':
      sys.exit()  # quit the program
     if player_move == 'r' or player_move == 'p' or player_move == 's':
        break  # break out of the player loop.
     print('Type one of r, p, s, or q.')

# Display what the player chose:

    if player_move == 'r':
        print('Rock versus...')
    elif player_move == 'p':
        print('Paper versus...')
    elif player_move == 's':
        print('Scissors versus...')

# Display what the computer chose:

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('Paper')
    elif random_number == 3:
        computer_move = 's'
        print('Scissors')

# Display and record the win/loss/tie

    if player_move == computer_move:
            print('It is a tie!')
            ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
            print('You win!')
            wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
            print('You win!')
            wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
            print('You Win!')
            wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
            print('You lose!')
            losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
            print('You lose!')
            losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
            print('You lose!')
            losses = losses + 1
