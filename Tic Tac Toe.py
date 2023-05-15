import random
board1 = [1, 2, 3]
board2 = [4, 5, 6]
board3 = [7, 8, 9]
lines = "----------"

bigBoard = [board1, board2, board3]
winCondition = 0


def update_board():
    output = ""
    linesCounter = 0
    print("\n")
    for boards in bigBoard:
        counter = 0
        for positions in boards:
            output += str(positions)
            if counter < 2:
                output += str(" | ")
                counter = counter + 1
        if linesCounter < 2:
            output += "\n"
            output += lines
            output += "\n"
            linesCounter +=  1 
    return output

print(update_board())


def win_check_horizontal():
    n = len(bigBoard)
    win = 0
    winner = ""
    for positionCheck in range(n):
        if bigBoard[positionCheck][0] == bigBoard[positionCheck][1] and bigBoard[positionCheck][1] == bigBoard[positionCheck][2]:
            win = 2
            winner = bigBoard[positionCheck][0]
    return (win, winner)


def win_check_vertical():
    n = len(bigBoard)
    win = 0
    winner = ""
    for positionCheck in range(n):
        if bigBoard[0][positionCheck] == bigBoard[1][positionCheck] and bigBoard[1][positionCheck] == bigBoard[2][positionCheck]:
            win = 2
            winner = bigBoard[0][positionCheck]
    return (win, winner)
 

def win_check_diagonal_TL_BR():
    n = len(bigBoard)
    win = 0
    winner = ""
    positionCheck = 0
    if bigBoard[positionCheck][positionCheck] == bigBoard[positionCheck + 1][positionCheck + 1] and bigBoard[positionCheck + 1][positionCheck + 1] == bigBoard[positionCheck + 2][positionCheck + 2]:
        win = 2
        winner = bigBoard[positionCheck][positionCheck]

    return (win, winner)
        
  

def win_check_diagonal_BL_TR():
    n = len(bigBoard)
    win = 0
    winner = 0
    positionCheck = 0
    positionSum = 2 - positionCheck
    if bigBoard[positionCheck][positionSum] == bigBoard[positionCheck + 1][positionSum - 1] and bigBoard[positionCheck + 1][positionSum - 1] == bigBoard[positionCheck + 2][positionSum - 2]:
        win = 2
        winner = bigBoard[positionCheck][positionSum]
    return (win, winner)

update_board()
n = len(bigBoard)
turnCounter = 0
while winCondition != 1:
    if win_check_horizontal()[0] > 1:
        winCondition = 1
        print("You win! " + win_check_horizontal()[1])
    if win_check_vertical()[0] > 1:
        winCondition = 1
        print("You win! " + win_check_vertical()[1])
    if  win_check_diagonal_BL_TR()[0] > 1:
        winCondition = 1
        print("You win! " + win_check_diagonal_BL_TR()[1])
    if win_check_diagonal_TL_BR()[0] > 1:
        winCondition = 1
        print("You win! " + win_check_diagonal_TL_BR()[1])

    if turnCounter == 0:
        player = int(input("Enter a position "))
        for positionCheck in range(n):
            for positionCheckAgain in range(n):
                if bigBoard[positionCheck][positionCheckAgain] == player:
                    bigBoard[positionCheck][positionCheckAgain] = "x"
                    print(update_board())  
                    turnCounter = 1
        

    botCheck = 0 # 0 = new move, 1 = already changed
    while turnCounter == 1:
        bot = random.randrange(1, 10)
        if botCheck == 0:
            for positionCheck in range(n):
                for positionCheckAgain in range(n):
                    if bigBoard[positionCheck][positionCheckAgain] == bot:
                            bigBoard[positionCheck][positionCheckAgain] = "O"
                            print(update_board())
                            turnCounter = 0 







#     bot = random.randrange(1,10)
#     for positionCheck in range(n):
#         for positionCheckAgain in range(n):
#             if bigBoard[positionCheck][positionCheckAgain] == bot:
#                 bigBoard[positionCheck][positionCheckAgain] = "O"
#                 turnCounter = 0
#     if win_check_horizontal()[0] > 1 or win_check_vertical()[0] > 1 or win_check_diagonal_BL_TR()[0] > 1 or win_check_diagonal_TL_BR()[0] > 1:
#         winCondition = 1
#         print("Bot wins!")     
# # Need to see who actually wins






    # if player < 4:
    #     board1[player] = "x"
    # if player < 7:
    #     player -= 4
    #     board2[player] = "x"
    # if player < 10:
    #     player -= 7
    #     board3[player] = "x"

 
    
        







# print(str(bigBoard[0]) + "\n" + lines + "\n" + str(bigBoard[1]) + "\n" + lines + "\n" + str(bigBoard[2]))


