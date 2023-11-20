sizeX = 7
sizeY = 6

def checkDraw(board):
    if ~(board[0] | board[1]) == 0:
        return True
    return False

def checkWin(board, player):
    if board[player-1] & board[player-1] << 8  & board[player-1] << 16 & board[player-1] << 24  != 0: return True
    if board[player-1] & board[player-1] << 1  & board[player-1] << 2  & board[player-1] << 3   != 0: return True
    if board[player-1] & board[player-1] << 7  & board[player-1] << 14 & board[player-1] << 21  != 0: return True
    if board[player-1] & board[player-1] << 9  & board[player-1] << 18 & board[player-1] << 27  != 0: return True
    return False
    
def isFinished(board):
    if checkWin(board, 1) or checkWin(board, 2) or checkDraw(board):
        return True
    return False


def getBoardEval(board, player):
    if checkWin(board, player):
        return 50
    if checkWin(board, 3-player):
        return -50
    doDraw = checkDraw(board)
    if doDraw:
        return 0

    evaluation = 0
    evaluation += bin(board[player-1] & board[player-1] << 8)[2:].count("1")
    evaluation += bin(board[player-1] & board[player-1] << 1)[2:].count("1")
    evaluation += bin(board[player-1] & board[player-1] << 7)[2:].count("1")
    evaluation += bin(board[player-1] & board[player-1] << 9)[2:].count("1")
    
    evaluation -= bin(board[3-player-1] & board[3-player-1] << 8)[2:].count("1")
    evaluation -= bin(board[3-player-1] & board[3-player-1] << 1)[2:].count("1")
    evaluation -= bin(board[3-player-1] & board[3-player-1] << 7)[2:].count("1")
    evaluation -= bin(board[3-player-1] & board[3-player-1] << 9)[2:].count("1")
    
    return evaluation

def getHashFromBoard(board):
    return int(bin(board[0])[2:]) + int(bin(board[1])[2:]) * 2