import random
# coin flip
def coin_flip():
    player1Name = 0
    player2Name = 1
    whichPlayer = 0 # 0 = no one, 1 = player1, 2 = player 2
    player1CoinCall = 0
    player2CoinCall = 0
    randomTurnToCall = random.randrange(2)
    if randomTurnToCall == player1Name:
        player1Name = input("Enter your name: ")
        player2Name = input("Enter another person's name: ")
        player1CoinCall = input(player1Name + ". Enter H or T: ")
        whichPlayer = 1
    if randomTurnToCall == player2Name:
        player1Name = input("Enter your name: ")
        player2Name = input("Enter another player's name: ")
        player2CoinCall = input(player2Name + ". Enter H or T: ")
        whichPlayer = 2

    randomflip = random.randrange(2)
    if player1CoinCall == "H" :
        player1CoinCall = 0
    if player1CoinCall == "T":
        Player1CoinCall = 1
    if player2CoinCall == "H":
        player2CoinCall = 0
    if player2CoinCall == "T":
        player2CoinCall = 1

    if whichPlayer == 1 and randomflip == player1CoinCall:
        print(player1Name + " goes first.")
    if whichPlayer == 1 and randomflip != player1CoinCall:
        print(player2Name + " goes first.")
    if whichPlayer == 2 and randomflip == player2CoinCall:
        print(player2Name + " goes First.")
    if whichPlayer == 2 and randomflip != player2CoinCall:
        print(player1Name + " goes first.")
#-----------------------------------------------------------
coin_flip()

board1 = [" ", " ", " ", " ", " ", " ", " ", " "]
board2 = [" ", " ", " ", " ", " ", " ", " ", " "]
board3 = [" ", " ", " ", " ", " ", " ", " ", " "]
board4 = [" ", " ", " ", " ", " ", " ", " ", " "]
board5 = [" ", " ", " ", " ", " ", " ", " ", " "]
board6 = [" ", " ", " ", " ", " ", " ", " ", " "]
board7 = [" ", " ", " ", " ", " ", " ", " ", " "]
board8 = [" ", " ", " ", " ", " ", " ", " ", " "]
hLine = "   +---+---+---+---+---+---+---+---+"

bigBoard = [board1, board2, board3, board4, board5, board6, board7, board8]
winCondition = 0
n = len(bigBoard)

#game start
board4[3] = "X"
board4[4] = "O"
board5[3] = "O"
board5[4] = "X"

def update_board():
    output = ('     1   2   3   4   5   6   7   8')
    output += "\n"
    output += hLine
    output += "\n"
    for i in range(n):
        output += str(i + 1) + " "
        for j in range(n):
            output += " | " + str(bigBoard[i][j])
            if j == 7: 
                output += " | "
                output += "\n"
                output += hLine
                output += "\n"
    return output  

print(update_board())

print("Type 'x' to end the game.")

#player points counters --------------------------------------
def player1_counter():
    player1Counter = 0
    for i in range(n): 
        for j in range(n):
            if bigBoard[j][i] == "X":
                player1Counter += 1
    return player1Counter

def player2_counter():
    player2Counter = 0
    for i in range(n): 
        for j in range(n):
            if bigBoard[j][i] == "O":
                player2Counter += 1
    return player2Counter
# --------------------------------------
#horizontal_position_checks
def horizontal_position_check(x, y):
    horizontalLeftCounter = 1
    horizontalRightCounter = 1
    hLeftCheck = 0
    hRightCheck = 0

    while x - horizontalLeftCounter > -1:
        if bigBoard[y][x] != bigBoard[y][x - horizontalLeftCounter] and bigBoard[y][x - horizontalLeftCounter] != " " and x - horizontalRightCounter != 0:
            horizontalLeftCounter += 1
            hLeftCheck += 1
        elif bigBoard[y][x - horizontalLeftCounter] == " ":
            hLeftCheck = 0
            break
        else:
            break
        if x - horizontalLeftCounter == 0:
            if bigBoard[y][0] == bigBoard[y][x]:
                break
            else:
                hLeftCheck = 0
                break


    while x + horizontalRightCounter < 8:
        if bigBoard[y][x] != bigBoard[y][x + horizontalRightCounter] and bigBoard[y][x + horizontalRightCounter] != " " and x + horizontalRightCounter != 7:
            horizontalRightCounter += 1
            hRightCheck += 1
        elif bigBoard[y][x + horizontalRightCounter] == " ":
            hRightCheck = 0
            break
        else:
            break

        if x + horizontalRightCounter == 7:
            if bigBoard[y][7] == bigBoard[y][x]:
                break
            else:
                hRightCheck = 0
                break


    return hLeftCheck, hRightCheck
#--------------------------------------------
#change of pieces horizontal
def change_pieces_horizontal(x, y, px, py): # x = left, y = right, p= player's position
    # print(px)
    # print(py)
    for i in range(x):
        bigBoard[py][px - i - 1] = bigBoard[py][px]
    for j in range(y):
        bigBoard[py][px + j + 1] = bigBoard[py][px]
#-------------------------------------------------------------
#vertical_position_check
def vertical_position_check(x, y):
    verticalUpCounter = 1
    verticalDownCounter = 1
    vUpCheck = 0
    vDownCheck = 0

    while y - verticalUpCounter > -1:
        if bigBoard[y][x] != bigBoard[y - verticalUpCounter][x] and bigBoard[y - verticalUpCounter][x] != " " and y - verticalUpCounter != 0:
            verticalUpCounter += 1
            vUpCheck += 1
        elif bigBoard[y - verticalUpCounter][x] == " ":
            vUpCheck = 0
            break
        else:
            break

        if y - verticalUpCounter == 0:
            if bigBoard[0][x] == bigBoard[y][x]:
                break
            else:
                vUpCheck = 0
                break

    while y + verticalDownCounter < 8:
        if bigBoard[y][x] != bigBoard[y + verticalDownCounter][x] and bigBoard[y + verticalDownCounter][x] != " " and y + verticalDownCounter != 7:
            verticalDownCounter += 1
            vDownCheck += 1
        elif bigBoard[y + verticalDownCounter][x] == " ":
            vDownCheck = 0
            break
        else:
            break

        if y + verticalDownCounter == 7:
            if bigBoard[7][x] == bigBoard[y][x]:
                break
            else:
                vDownCheck = 0
                break


    return vUpCheck, vDownCheck
#----------------------------------------
#change pieces vertical
def change_pieces_vertical(x, y, px, py): # x = up, y = down, p= player's position
    # print(px)
    # print(py)
    for i in range(x):
        bigBoard[py - i - 1][px] = bigBoard[py][px]
    for j in range(y):
        bigBoard[py + j + 1][px] = bigBoard[py][px]
#--------------------------------------------------
# diagonal position check TL BR
def diagonal_position_TL_BR_check(x, y):
    diagonalBRTLCounter = 1
    diagonalTLBRCounter = 1
    dBRTLCheck = 0
    dTLBRCheck = 0

    while y - diagonalBRTLCounter > -1 and x - diagonalBRTLCounter > -1 :
        if bigBoard[y][x] != bigBoard[y - diagonalBRTLCounter][x - diagonalBRTLCounter] and bigBoard[y - diagonalBRTLCounter][x - diagonalBRTLCounter] != " " and y - diagonalBRTLCounter != 0 and x - diagonalBRTLCounter != 0:
            diagonalBRTLCounter += 1
            dBRTLCheck += 1
        elif bigBoard[y - diagonalBRTLCounter][x - diagonalBRTLCounter] == " ":
            dBRTLCheck = 0
            break
        else:
            break
    
        if y - diagonalBRTLCounter == 0 or x - diagonalBRTLCounter == 0:
            if bigBoard[0][x - diagonalBRTLCounter] == bigBoard[y][x] or bigBoard[y - diagonalBRTLCounter][0] == bigBoard[y][x]: #need to check logic
                break
            else:
                dBRTLCheck = 0
                break

    while x + diagonalTLBRCounter < 8 and y + diagonalTLBRCounter < 8:
        if bigBoard[y][x] != bigBoard[y + diagonalTLBRCounter][x + diagonalTLBRCounter] and bigBoard[y + diagonalTLBRCounter][x + diagonalTLBRCounter] != " " and x + diagonalTLBRCounter != 7 and y + diagonalTLBRCounter != 7:
            diagonalTLBRCounter += 1
            dTLBRCheck += 1
        elif bigBoard[y + diagonalTLBRCounter][x + diagonalTLBRCounter] == " ":
            dTLBRCheck = 0
            break
        else:
            break

        if x + diagonalTLBRCounter == 7 or y + diagonalTLBRCounter == 7:
            if bigBoard[y + diagonalTLBRCounter][7] == bigBoard[y][x] or bigBoard[7][x + diagonalTLBRCounter] == bigBoard[y][x]:
                break
            else:
                dTLBRCheck = 0
                break

    return dBRTLCheck, dTLBRCheck
#--------------------------------------------------------------------
# change of pieces diagonal TL BR
def change_pieces_diagonal_TL_BR(x, y, px, py): # x = BRTL, y = TLBR, p= player's position

    for i in range(x):
        bigBoard[py - i - 1][px - i - 1] = bigBoard[py][px]
    for j in range(y):
        bigBoard[py + j + 1][px + j + 1] = bigBoard[py][px]
#-----------------------------------------
#diagonal position check BL TR
def diagonal_position_BL_TR_check(x, y):
    diagonalBLTRCounter = 1
    diagonalTRBLCounter = 1
    dBLTRCheck = 0
    dTRBLCheck = 0
    while y - diagonalBLTRCounter > -1 and x + diagonalBLTRCounter < 8:
        if bigBoard[y][x] != bigBoard[y - diagonalBLTRCounter][x + diagonalBLTRCounter] and bigBoard[y - diagonalBLTRCounter][x + diagonalBLTRCounter] != " " and y - diagonalBLTRCounter != 0 and x + diagonalBLTRCounter != 7:
            diagonalBLTRCounter += 1
            dBLTRCheck += 1
        elif bigBoard[y - diagonalBLTRCounter][x + diagonalBLTRCounter] == " ":
            dBLTRCheck = 0
            break
        else:
            break
    
        if y - diagonalBLTRCounter == 0 or x - diagonalBLTRCounter == 7:
            if bigBoard[0][x + diagonalBLTRCounter] == bigBoard[y][x] or bigBoard[y - diagonalBLTRCounter][7] == bigBoard[y][x]: #need to check logic
                break
            else:
                dBLTRCheck = 0
                break

    while x - diagonalTRBLCounter > -1 and y + diagonalTRBLCounter < 8:
        if bigBoard[y][x] != bigBoard[y + diagonalTRBLCounter][x - diagonalTRBLCounter] and bigBoard[y + diagonalTRBLCounter][x - diagonalTRBLCounter] != " " and x - diagonalTRBLCounter != 0 and y + diagonalTRBLCounter != 7:
            diagonalTRBLCounter += 1
            dTRBLCheck += 1
        elif bigBoard[y + diagonalTRBLCounter][x - diagonalTRBLCounter] == " ":
            dTRBLCheck = 0
            break
        else:
            break

        if x - diagonalTRBLCounter == 0 or y + diagonalTRBLCounter == 7:
            if bigBoard[y + diagonalTRBLCounter][0] == bigBoard[y][x] or bigBoard[7][x - diagonalTRBLCounter] == bigBoard[y][x]:
                break
            else:
                dTRBLCheck = 0
                break

    return dBLTRCheck, dTRBLCheck
#--------------------------------------------------
#change of pieces diagonal BL TR
def change_pieces_diagonal_BL_TR(x, y, px, py): # x = BLTR, y = TRBL, p= player's position

    for i in range(x):
        bigBoard[py - i - 1][px + i + 1] = bigBoard[py][px]
    for j in range(y):
        bigBoard[py + j + 1][px - j - 1] = bigBoard[py][px]
#---------------------------------
#Win check
def win_check():
    emptySpaceCounter = 0
    win = 0

    for i in range(n):
        for j in range(n):
            if bigBoard[j][i] == " ":
                emptySpaceCounter += 1

    if emptySpaceCounter == 0:
        win = 1
    return emptySpaceCounter, win
#---------------------------

# Game Function
turnCounter = 0
while winCondition != 1:
    isItOver = win_check()
    if isItOver[1] == 1:
        if player1_counter() > player2_counter():
            print("Game Over! Player 1 Wins!")
            winCondition = 1
            break
        elif player2_counter() > player1_counter():
            print("Game Over! Player 2 Wins")
            winCondition = 1
            break
        else:
            print("Game Over! Draw!")
            winCondition = 1
            break
# actual game 
    while turnCounter == 0: #player 1
        player1 = input("Player 1: Enter a position ")
        if len(player1) == 2:
            if int(player1) > 88 or int(player1) < 11:
                print("Error. Invalid Input.")
            else: 
                player1x = int(player1[0]) - 1
                player1y = int(player1[1]) - 1
                if player1y == 8 or player1y == -1: #need to implement for player 2
                    print("Error. Invalid Input.")
                else:
                    if bigBoard[player1y][player1x] == "X" or bigBoard[player1y][player1x] == "O":
                        print("Error. Invalid Input.")
                    else:
                        bigBoard[player1y][player1x] = "X"
                        horizontalResult = horizontal_position_check(player1x, player1y)
                        verticalResult = vertical_position_check(player1x, player1y)
                        diagonalResultTLBR = diagonal_position_TL_BR_check(player1x, player1y)
                        diagonalResultBLTR = diagonal_position_BL_TR_check(player1x, player1y)
                        turnCounter = 1
                        change_pieces_horizontal(horizontalResult[0], horizontalResult[1], player1x, player1y)
                        change_pieces_vertical(verticalResult[0], verticalResult[1], player1x, player1y)
                        change_pieces_diagonal_TL_BR(diagonalResultTLBR[0], diagonalResultTLBR[1], player1x, player1y)
                        change_pieces_diagonal_BL_TR(diagonalResultBLTR[0], diagonalResultBLTR[1], player1x, player1y)
                        print(update_board())
                        print("There are " + str(win_check()[0]) + " empty spots left.")
                        print("Player 1 Points: " + str(player1_counter()))
                        print("Player 2 Points: " + str(player2_counter()))
        elif player1 == "x":
                winCondition = 1
                break
        else:
                print("Error. Invalid Input.")


    while turnCounter == 1: #player 2
        player2 = input("Player 2: Enter a position ")
        if len(player2) == 2:
            if int(player2) > 88 or int(player2) < 11:
                print("Error. Invalid Input.")
            else: 
                player2x = int(player2[0]) - 1
                player2y = int(player2[1]) - 1
                if bigBoard[player2y][player2x] == "X" or bigBoard[player2y][player2x] == "O":
                    print("Error. Invalid Input.")
                else:    
                    bigBoard[player2y][player2x] = "O"
                    horizontalResults = horizontal_position_check(player2x, player2y) # s = player 2
                    verticalResults = vertical_position_check(player2x, player2y)
                    diagonalResultTLBRs = diagonal_position_TL_BR_check(player2x, player2y)
                    diagonalResultBLTRs = diagonal_position_BL_TR_check(player2x, player2y)
                    turnCounter = 0
                    change_pieces_horizontal(horizontalResults[0], horizontalResults[1], player2x, player2y)
                    change_pieces_vertical(verticalResults[0], verticalResults[1], player2x, player2y)
                    change_pieces_diagonal_TL_BR(diagonalResultTLBRs[0], diagonalResultTLBRs[1], player2x, player2y)
                    change_pieces_diagonal_BL_TR(diagonalResultBLTRs[0], diagonalResultBLTRs[1], player2x, player2y)
                    print(update_board())
                    print("There are " + str(win_check()[0]) + " empty spots left.")
                    print("Player 1 Points: " + str(player1_counter()))
                    print("Player 2 Points: " + str(player2_counter()))
        elif player2 == "x":
                winCondition = 1
                break
        else:
                print("Error. Invalid Input.")





