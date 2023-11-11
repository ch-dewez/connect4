sizeX = 7
sizeY = 6

def checkVertical(board, player, x):
    pieceInLine = 0
    for y in range(sizeY):
        if board[y][x] == player:
            pieceInLine += 1
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True
    return False

def checkHorizontal(board, player, y):
    pieceInLine = 0
    for x in range(sizeX):
        if board[y][x] == player:
            pieceInLine += 1
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True
    return False

def checkDraw(board):
    for x in range(sizeX):
        if (board[0][x] == 0):
            return False
    return True

def checkDiagonalSWNE(board, player, x, y):
    checkX = x
    checkY = y
    pieceInLine = 0

    while checkX < sizeX and checkY < sizeY:
        if board[checkY][checkX] == player:
            pieceInLine += 1
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True
        checkX += 1
        checkY -= 1
    return False

def checkDiagonalSENW(board, player, x, y):
    checkX = x
    checkY = y
    pieceInLine = 0
    while checkX >= 0 and checkY < sizeY:
        if board[checkY][checkX] == player:
            pieceInLine += 1
        else:
            pieceInLine = 0
        if pieceInLine == 4:
            return True
        checkX -= 1
        checkY -= 1
    return False



def checkWinLastMove(x, y, player, board):
    # check vertical
    if checkVertical(board, player, x):
        return True

    # check horizontal
    if checkHorizontal(board, player, y):
        return True

    # check diagonal SW -> NE

    # get first piece in diagonal
    firstX = x
    firstY = y
    while True:
        if firstX == 0 or firstY == 0:
            break
        firstX -= 1
        firstY += 1 # SW -> NE [0] is top

    if checkDiagonalSWNE(board, player, firstX, firstY):
        return True
    
    # check diagonal SE -> NW

    # get first piece in diagonal
    firstX = x
    firstY = y
    while True:
        if firstX == sizeX - 1 or firstY == 0:
            break
        firstX -= 1
        firstY += 1 # SE -> NW [0] is top
    
    if checkDiagonalSENW(board, player, firstX, firstY):
        return True

    return False

def checkWinFullBoard(board, player):
    #check all vertical lines
    for x in range(sizeX):
        if checkVertical(board, player, x):
            return True

    for y in range(sizeY):
        if checkHorizontal(board, player, y):
            return True

    # check diagonals SW -> NE
    # all first X
    firstX = [0, 0, 0, 1, 2, 3]
    # all first Y
    firstY = [3, 4, 5, 5, 5, 5]

    for i in range(len(firstX)):
        if checkDiagonalSWNE(board, player, firstX[i], firstY[i]):
            return True

    # check diagonals SE -> NW
    # all first X
    firstX = [6, 6, 6, 5, 4, 3]
    # all first Y
    firstY = [3, 4, 5, 5, 5, 5]

    for i in range(len(firstX)):
        if checkDiagonalSENW(board, player, firstX[i], firstY[i]):
            return True

    return False


def getBoardEval(board, player):
    if checkWinFullBoard(board, player):
        return 100
    if checkWinFullBoard(board, 3 - player):
        return -100
    if checkDraw(board):
        return 0

    return 0