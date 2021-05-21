# -*- coding: utf-8 -*-
"""
2 player not done, but sort of works

1 player works 

I have only tested in IDE

output formatting not complete

"""
import random

print('Welcome! make a selection 1-9')
theBoard= {'1': '1', '2': '2', '3': '3','4': '4', '5': '5', '6': '6','7': '7', '8': '8', '9': '9'}
print(theBoard)


#prints the board
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' +  board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    
#puts the board dictionary values in a list and for every X or O add 1 to x list. When x list is at 9 the board is full
def fullboard(theBoard):
    #num = '1','2','3','4','5','6','7','8','9'
    x = 0
    #num = [i for i in range(1,10)]
    stuff= list(theBoard.values())
    for item in stuff:
        if item == 'X' or item == 'O':
            x+=1
            
    if x == 9:
        return True
    else:
        return False
            
            

    
#printBoard(theBoard)
####
# Asks to choose a location, then checks to make sure its not already taken
##
def locationCheck(board, selection): #Broke???****
     if board[selection] == 'X' or board[selection] == 'O' :
         print('Already chosen')
         playerChoice(board)
     else:
         return False
        

def playerChoice(aboard): #Broke??****
    #chose a location on the board and verifies
    choice=input("Choose Location: ")
    checkRange = [i for i in range(1,10)]
    if choice in str(checkRange):
        return choice
        # if locationCheck(aboard, choice) == False:
        #     return choice
    else:
        print('choose a number between 1 and 9')

##
# Asks how many players and checks input
####

def playerCount():
    #select how many players and X O values
    global player1
    global player2
    global players
    global computerPlayer
    player_count = input('1 or 2 players:\n')
    if player_count == str(1):
        player1 = input('X or O?\n').upper()
        players['turn'] = 'player_1'
        computerPlayer= True
        if player1 == 'X' or player1 == 'O':
            if player1 == 'X':  
                players['player_2']= 'O'
                players['player_1']= 'X'
            else:
                players['player_2'] = 'X'
                players['player_1']= "O"
            print('Single player. \nPlayer 1 is: ' + players['player_1'] + " and the computer is: " + players['player_2'] )
        else:
            print('You did not enter a X or O')
            playerCount()
            
            
    elif player_count == str(2):
        print('Two players')
        chooser= random.randint(1, 2) # random player to choose x or o
        if chooser == 1:
            player1 = input('Player 1 choose X or O\n').upper()
            players['turn'] = 'player_1'
            if player1 == 'X' or player1 == 'O':
                if player1 == 'X':  
                    players['player_2'] = 'O'
                    players['player_1'] = 'X'
                else:
                    players['player_2'] = 'X'
                    players['player_1']= "O"
                print('Two player. \nPlayer 1 is: ' + players['player_1'] + " and Player 2 is: " + players['player_2']) 
            else:
                print('You did not enter a X or O')
                playerCount()
        else:
            player2= input('Player 2 choose X or O\n')
            players['turn'] = 'player_2'
            if player2.upper() == 'X' or player2.upper() == 'O':
                if player2.upper() == 'X':  
                    players['player_1'] = 'O'
                    players['player_2'] = 'X'
                else:
                    players['player_1'] = 'X'
                    players['player_2']= "O"
                print('Two Player. \nPlayer 1 is: ' + players['player_1'] + " and Player 2 is: " + players['player_2']) 
            else:
                print('You did not enter a X or O')
                playerCount()


    else:
        print('You did not pick a 1 or 2')
        playerCount()

#swaps turns
def swapPlayer(currentPlayer):
    if str(currentPlayer) == "player_1":
        return 'player_2'
    elif str(currentPlayer) == "player_2":
        return 'player_1'



#for the computer to pick a location on the board
def randomPick():
    #Computer random pick a loation
    computerChoice= random.randint(1, 9)
    return computerChoice


def winCheck(bboard):
    if bboard['1'] == bboard['2'] == bboard['3'] or \
        bboard['4'] == bboard['5'] ==bboard['6'] or \
        bboard['7'] == bboard['8'] ==bboard['9'] or \
        bboard['1'] == bboard['5'] ==bboard['9'] or \
        bboard['1'] == bboard['4'] ==bboard['7'] or \
        bboard['2'] == bboard['5'] ==bboard['8'] or \
        bboard['3'] == bboard['6'] ==bboard['9'] or \
        bboard['3'] == bboard['5'] ==bboard['7'] :
            return True
    else:
        return False
#will be for 2 player to see who goes first
def randomFirstTurn():
    who= random.randint(1, 2)
    if who == 1:
        return 'player_1'
    else:
        return 'player_2'
    
# checks the input when picking a location on the board
def playerInputCheck(choice):
    # choice=input("Choose Location: ")
    checkRange = [i for i in range(1,10)]
    while choice not in str(checkRange):
        print('Pick a number between 1 and 9\n')
        choice=input("Choose Location:\n ")
    else:
        
        return choice
    
    


# player1 = {'player_1':''} # X or O
# player2 = {'player_2': ''} #  X or O
players= {'player_2': '','player_1':'','turn':''}
current_player = ''
computerPlayer= False



gameOn = True
gameOver= False
while gameOn == True:
    playerCount()
    #whosTurn = randomFirstTurn()
    #current_player = randomFirstTurn()
    if computerPlayer == True:
        print("Player 1 will go first and the computer will be player 2")
        while gameOver == False:
            #while winCheck(theBoard) == False or fullboard(theBoard) == False:
            
            #whosturn = player1
            
            print(players['turn'] + "\'s turn | "+ players[players['turn']])
            print('\n')
            
            printBoard(theBoard)
            
            # player 1 turn
            if players['turn'] == 'player_1':
                player1choice = input('Pick a location: \n') # asks for location
                playerInputCheck(player1choice) # checks the input
                
                while theBoard[str(player1choice)] == "X" or theBoard[str(player1choice)] == "O" : # will keep asking if the picked location is already a X or a O
                    
                    player1choice = input('Pick another location: \n')
                        
                else:
                                        
                    theBoard[player1choice] = players[players['turn']] # changes the dictionary value 
                
                    print('\n'*2)
            #player 2 turn
            else:
                
                comp_choice = randomPick() # computers choice
                
                while theBoard[str(comp_choice)] == "X" or theBoard[str(comp_choice)] == "O": # will keep picking another random number if the location is already a X or O
                    if fullboard(theBoard) == True:
                        break
                    else:
                   
                        comp_choice = randomPick()
                        print('computer picking another number\n')
               
                else:
                 
                    print('the computer picked: ' + str(comp_choice))
                    print('\n')
                    theBoard[str(comp_choice)] = players['player_2']
            
            
          
            
            print('\n' * 10)
            
            if winCheck(theBoard) == True or fullboard(theBoard) == True: # win and full board checks
                if winCheck(theBoard) == True:
                    
                    print("Game Over " + players['turn'] + ' wins! \n')
                    printBoard(theBoard)
                    gameOn = False
                    break
               
                elif fullboard(theBoard) == True:
                    print('Tie Game\n')
                    printBoard(theBoard)
                    gameOn= False
                    break
                
            
            players['turn'] = swapPlayer(players['turn']) # changes the turn value 
            
        # 2 player not done
    else:
        while winCheck(theBoard) == False:
            #whosturn = player1
            
            print(players['turn'] + "\'s Turn")
            
            printBoard(theBoard)
            
            
            theBoard[playerChoice(theBoard)] = players[players['turn']]
            
            
            printBoard(theBoard)
            
                    
            players['turn'] = swapPlayer(players['turn'])
            
            print('\n' * 50)
            
            if winCheck(theBoard) == True:
               gameOn = False
        







