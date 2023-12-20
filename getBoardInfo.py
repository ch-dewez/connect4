sizeX = 7
sizeY = 6

def checkDraw(board):
    if ~(board[0] | board[1]) == 0:
        return True
    return False

def checkWin(board, player):
    if board[player-1] & board[player-1] << 8  & board[player-1] << 16 & board[player-1] << 24  != 0: return True
    if board[player-1] & board[player-1] >> 1  & board[player-1] >> 2  & board[player-1] >> 3   != 0: return True
    if board[player-1] & board[player-1] << 7  & board[player-1] << 14 & board[player-1] << 21  != 0: return True
    if board[player-1] & board[player-1] << 9  & board[player-1] << 18 & board[player-1] << 27  != 0: return True
    return False
    
def isFinished(board):
    if checkWin(board, 1) or checkWin(board, 2) or checkDraw(board):
        return True
    return False


def getBoardEval(board, player):
    if checkWin(board, player):
        return 500
    if checkWin(board, 3-player):
        return -500
    doDraw = checkDraw(board)
    if doDraw:
        return -10

    evaluation = 0
    
    evaluation += getEvalForOnePlayer(board, player)
    evaluation -= getEvalForOnePlayer(board, 3-player)
    
    return evaluation

def getEvalForOnePlayer(board, player):
    evaluation = 0
    pieces = board[0] | board[1]
    
    # for the player
    # for row of 2
    verticalConnection = board[player-1] & board[player-1] << 8
    evaluation += bin(verticalConnection & ~pieces >> (8*2))[2:].count("1")
    
    horizontalConnection = board[player-1] & board[player-1] << 1
    evaluation += bin((horizontalConnection & ~pieces << 1) | (horizontalConnection & (~pieces >> 2)))[2:].count("1")
    
    obliqueConnection = board[player-1] & board[player-1] << 7
    evaluation += bin((obliqueConnection & ~pieces >> 7) | (obliqueConnection & (~pieces << (7*2))))[2:].count("1")
    
    obliqueConnection2 = board[player-1] & board[player-1] << 9
    evaluation += bin((obliqueConnection2 & ~pieces >> 9) | (obliqueConnection2 & (~pieces << (9*2))))[2:].count("1")
    
    # for row of 3
    verticalConnection &= board[player-1] << (8*2)
    evaluation += 2*bin(verticalConnection & ~pieces >> (8*3))[2:].count("1")
    
    horizontalConnection &= board[player-1] << 2
    evaluation += 2 * bin((horizontalConnection & ~pieces << 1) | (horizontalConnection & (~pieces >> 3)))[2:].count("1")
    
    obliqueConnection &= board[player-1] << (7*2)
    evaluation += 2*bin((obliqueConnection & ~pieces >> 7) | (obliqueConnection & (~pieces << (7*3))))[2:].count("1")
    
    obliqueConnection2 &= board[player-1] << (9*2)
    evaluation += 2*bin((obliqueConnection2 & ~pieces >> 9) | (obliqueConnection2 & (~pieces << (9*3))))[2:].count("1")
    
    return evaluation

def getHashFromBoard(board):
    return int(bin(board[0])[2:]) + int(bin(board[1])[2:]) * 2