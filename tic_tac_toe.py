# board , ply inp, check win tie,switch , check win tie

import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

c_ply = "x"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + "|" +board[1] + "|" + board[2] )
    print("------")
    print(board[3] + "|" +board[4] + "|" + board[5] )
    print("------")
    print(board[6] + "|" +board[7] + "|" + board[8] )
#printBoard(board)

def ply_inp(board):
    inp = int(input("enter pos 1-9: "))
    #inp = int(inp)
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = c_ply
    else:
        print("already filled spot")

def checkhorizontle(board):
    global winner 
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]

def checkver(board):
    global winner 
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True
    
def checkdiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[3]
        return True 
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True


def checkTie(board):
    if "-" not in board:
        print(board)
        
        print("------its a Tie------")
        gameRunning= False

def checkWin(board):
    if checkhorizontle(board) or checkhorizontle(board) or checkver(board) is True:
        print("the winner is" + winner)


def switchPlayer():
    global c_ply
    
    if c_ply == "x":
       c_ply = "0"
    else:
        c_ply = "x"

def computer(board):
    while c_ply == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()




while gameRunning:
    printBoard(board)
    ply_inp(board)
    checkWin(board)
    #checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)






