sizeX = 7
sizeY = 6

def checkDraw(board):
    if board[0] | board[1] == int("11111110111111101111111011111110111111101111111011111110", 2):
        return True
    return False

def checkWinFullBoard(board, player):
    if board[player-1] & board[player-1] << 8  & board[player-1] << 16 & board[player-1] << 24  != 0: return True
    if board[player-1] & board[player-1] << 1  & board[player-1] << 2  & board[player-1] << 3   != 0: return True
    if board[player-1] & board[player-1] << 7  & board[player-1] << 14 & board[player-1] << 21  != 0: return True
    if board[player-1] & board[player-1] << 9  & board[player-1] << 18 & board[player-1] << 27  != 0: return True
    return False
    
def isFinished(board):
    if checkWinFullBoard(board, 1) or checkWinFullBoard(board, 2) or checkDraw(board):
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
    evaluation += (board[player-1] & board[player-1] << 8).count(1)
    evaluation += (board[player-1] & board[player-1] << 1).count(1)
    evaluation += (board[player-1] & board[player-1] << 7).count(1)
    evaluation += (board[player-1] & board[player-1] << 9).count(1)
    
    evaluation += (board[3-(player-1)] & board[3-(player-1)] << 8).count(1)
    evaluation += (board[3-(player-1)] & board[3-(player-1)] << 1).count(1)
    evaluation += (board[3-(player-1)] & board[3-(player-1)] << 7).count(1)
    evaluation += (board[3-(player-1)] & board[3-(player-1)] << 9).count(1)
    
    return evaluation

def getHashFromBoard(board):
    return int(bin(board[0])[2:]) + int(bin(board[1])[2:]) * 2