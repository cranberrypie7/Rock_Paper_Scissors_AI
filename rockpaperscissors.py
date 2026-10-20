import random

MOVES=['rock','paper','scissors']
running = True
wins = 0
losses = 0
ties = 0
rounds = 0
moveHistory=[]
paper=0
rock=0
scissors=0

def computerMove():
    if (random.randrange(100)%2)==0:
        return MOVES[random.randrange(0,3)]
    else:
        if paper > rock and paper > scissors:
            return 'scissors'
        elif rock > paper and rock > scissors:
            return 'paper'
        elif scissors > paper and scissors > rock:
            return 'rock'
        else:
            return MOVES[random.randrange(0,3)]

while running == True:
    userMoves = input('Enter rock paper or scissors:')
    if userMoves == 'stop':
        running=False
        print(f'Wins:{wins} Losses:{losses} Ties:{ties} Winrate:{(wins/rounds)*100}')
        continue
    
    if userMoves not in MOVES:
        print('Enter a valid move')
        continue

    if rounds > 10:
        computer = computerMove()
    else:
        computer = MOVES[random.randrange(0,3)]

    rounds = rounds + 1
    if userMoves == 'rock':
        rock = rock + 1
        if computer == 'rock':
            print('Its a tie')
            ties = ties + 1
        elif computer == 'paper':
            print('You lose')
            losses = losses + 1
        else:
            print('You win')
            wins = wins + 1
    elif userMoves == 'paper':
        paper = paper + 1
        if computer == 'rock':
            print('You win')
            wins = wins + 1
        elif computer == 'paper':
            print('Its a tie')
            ties = ties + 1
        else:
            print('You lose')
            losses = losses + 1
    elif userMoves == 'scissors':
        scissors = scissors + 1
        if computer == 'rock':
            print('You lose')
            losses = losses + 1
        elif computer == 'paper':
            print('You win')
            wins = wins + 1
        else:
                print('Its a tie')
                ties=ties+1