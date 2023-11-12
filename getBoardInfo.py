sizeX = 7
sizeY = 6

def checkVertical(board, player, x):
    listOfPieceInLine = [0, 0]
    pieceInLine = 0
    for y in range(sizeY):
        if board[y][x] == player:
            pieceInLine += 1
        elif board[y][x] == 0:
            if pieceInLine == 2:
                listOfPieceInLine[0] += 1
            elif pieceInLine == 3:
                listOfPieceInLine[1] += 1
            pieceInLine = 0
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True, listOfPieceInLine
    return False, listOfPieceInLine

def checkHorizontal(board, player, y):
    pieceInLine = 0
    listOfPieceInLine = [0, 0]
    for x in range(sizeX):
        if board[y][x] == player:
            pieceInLine += 1
        elif board[y][x] == 0:
            if pieceInLine == 2:
                listOfPieceInLine[0] += 1
            elif pieceInLine == 3:
                listOfPieceInLine[1] += 1
            pieceInLine = 0
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True, listOfPieceInLine
    return False, listOfPieceInLine

def checkDraw(board):
    for x in range(sizeX):
        if (board[0][x] == 0):
            return False
    return True

def checkDiagonalSWNE(board, player, x, y):
    checkX = x
    checkY = y
    pieceInLine = 0
    listOfPieceInLine = [0, 0]

    while checkX < sizeX and checkY < sizeY:
        if board[checkY][checkX] == player:
            pieceInLine += 1
        elif board[y][x] == 0:
            if pieceInLine == 2:
                listOfPieceInLine[0] += 1
            elif pieceInLine == 3:
                listOfPieceInLine[1] += 1
            pieceInLine = 0
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True, listOfPieceInLine
        checkX += 1
        checkY -= 1
    return False, listOfPieceInLine

def checkDiagonalSENW(board, player, x, y):
    checkX = x
    checkY = y
    pieceInLine = 0
    listOfPieceInLine = [0, 0]
    while checkX >= 0 and checkY < sizeY:
        if board[checkY][checkX] == player:
            pieceInLine += 1
        elif board[y][x] == 0:
            if pieceInLine == 2:
                listOfPieceInLine[0] += 1
            elif pieceInLine == 3:
                listOfPieceInLine[1] += 1
            pieceInLine = 0
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True, listOfPieceInLine
        checkX -= 1
        checkY -= 1
    return False, listOfPieceInLine

def checkWinFullBoard(board, player):
    listOfPieceInLine = [0, 0]

    #check all vertical lines
    for x in range(sizeX):
        doWin, pieceInLine = checkVertical(board, player, x)
        listOfPieceInLine[0] += pieceInLine[0]
        listOfPieceInLine[1] += pieceInLine[1]
        if doWin:
            return True, listOfPieceInLine

    for y in range(sizeY):
        doWin, pieceInLine = checkHorizontal(board, player, y)
        listOfPieceInLine[0] += pieceInLine[0]
        listOfPieceInLine[1] += pieceInLine[1]
        if doWin:
            return True, listOfPieceInLine

    # check diagonals SW -> NE
    # all first X
    firstX = [0, 0, 0, 1, 2, 3]
    # all first Y
    firstY = [3, 4, 5, 5, 5, 5]

    for i in range(len(firstX)):
        doWin, pieceInLine = checkDiagonalSWNE(board, player, firstX[i], firstY[i])
        listOfPieceInLine[0] += pieceInLine[0]
        listOfPieceInLine[1] += pieceInLine[1]
        if doWin:
            return True, listOfPieceInLine

    # check diagonals SE -> NW
    # all first X
    firstX = [6, 6, 6, 5, 4, 3]
    # all first Y
    firstY = [3, 4, 5, 5, 5, 5]

    for i in range(len(firstX)):
        doWin, pieceInLine = checkDiagonalSENW(board, player, firstX[i], firstY[i])
        listOfPieceInLine[0] += pieceInLine[0]
        listOfPieceInLine[1] += pieceInLine[1]
        if doWin:
            return True, listOfPieceInLine

    return False, listOfPieceInLine

def isFinished(board):
    if checkWinFullBoard(board, 1)[0] or checkWinFullBoard(board, 2)[0] or checkDraw(board):
        return True
    return False


def getBoardEval(board, player):
    doWin, playerEval = checkWinFullBoard(board, player)
    if doWin:
        return 50
    doLose, otherPlayerEval = checkWinFullBoard(board, 3 - player)
    if doLose:
        return -50
    doDraw = checkDraw(board)
    if doDraw:
        return 0

    evaluation = 0
    for _ in range(playerEval[0]):
        evaluation += 1
    for _ in range(playerEval[1]):
        evaluation += 3

    for _ in range(otherPlayerEval[0]):
        evaluation -= 1
    for _ in range(otherPlayerEval[1]):
        evaluation -= 3

    return evaluation