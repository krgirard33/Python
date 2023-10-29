#Rock, Paper, Scissors game

import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: #Main Game Loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    
    while True: #Player input loop
        print('Enter your choice: (r)ock, (p)aper, (s)cissors, or (q)uit')
        
        playerChoice = input()
        
        if playerChoice == 'q':
            sys.exit() #Quit game
            
        if playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
            break #break out of player loop
            
        print('Type one of r, p, s, or q.') #They didn't pick a legal option
        
    #Display what the player chose
    if playerChoice == 'r':
        print('ROCK versus...')
    elif playerChoice == 'p':
        print('PAPER versus...')
    elif playerChoice == 's':
        print('SCISSORS versus...')
            
    #Display what the computer choose
    randomNumber = random.randint(1, 3)
        
    if randomNumber == 1:
        computerChoice = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerChoice = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerChoice = 's'
        print('SCISSORS')
            
    # Display and record the win/loss/tie
    if playerChoice == computerChoice:
        print('It is a tie')
        ties = ties + 1
    elif (playerChoice == 'r' and computerChoice == 's') or (playerChoice == 'p' and computerChoice == 'r') or (playerChoice == 's' and computerChoice == 'p'):
        print('You win!')
        wins = wins + 1
    elif (playerChoice == 'r' and computerChoice == 'p') or (playerChoice == 'p' and computerChoice == 's') or (playerChoice == 's' and computerChoice == 'r'):
        print('You lose')
        losses = losses + 1