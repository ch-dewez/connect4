import getBoardInfo

def makeAMove(board, collumn, playerToMove):
    maskForOneRow = 1 << getBoardInfo.sizeY + 1 - collumn # + 1 -> one collumn for easier comparaison
    mask = maskForOneRow | maskForOneRow << (getBoardInfo.sizeY + 2) | maskForOneRow << ((getBoardInfo.sizeY + 2) * 2) | maskForOneRow << ((getBoardInfo.sizeY + 2) * 3) | maskForOneRow << ((getBoardInfo.sizeY + 2) * 4) | maskForOneRow << ((getBoardInfo.sizeY + 2) * 5)
    height = bin((board[0] & mask) | ( board[1] & mask)).count("1")
    
    if height == getBoardInfo.sizeY:
        return False
    
    boardMove = 1 << (getBoardInfo.sizeX + 1) * height + getBoardInfo.sizeX - collumn
    newBoard = board.copy()
    newBoard[playerToMove-1] |= boardMove
    return newBoard

#  trying to make optimization 8 -> done -> don't do that much :(, 4 -> done -> big improvement
# , 9 -> done with bitboard, 3 -> done, 2 -> don't know how to do
# of https://larswaechter.dev/blog/minimax-performance-improvements/#:~:text=Improving%20Minimax%20performance%201%201.%20Alpha-Beta%20Pruning%20One,8.%20Improve%20.hasPlayerWon%20%28%29%20function%20...%20%C3%89l%C3%A9ments%20suppl%C3%A9mentaires

def minimax(board, depth, alpha, beta, maximizingPlayer, botNumber, storage = {}, heightMultiplier = 2):
    if depth == 0 or getBoardInfo.isFinished(board):
        return getBoardInfo.getBoardEval(board, botNumber) * heightMultiplier, 0, storage

    if maximizingPlayer:
        maxEval = -100000
        bestMove = 0
        for collumn in range(getBoardInfo.sizeX):
            newBoard = makeAMove(board, collumn, botNumber)
            if newBoard == False:
                continue
            hashBoard = getBoardInfo.getHashFromBoard(newBoard)
            
            if hashBoard in storage:
                evaluation = storage[hashBoard]
            else:
                evaluation, _, storage = minimax(newBoard, depth - 1, alpha, beta, False, botNumber, storage, heightMultiplier / 1.5)
                storage[hashBoard] = evaluation
            
            if (evaluation > maxEval):
                maxEval = evaluation
                bestMove = collumn
            
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval, bestMove, storage
    else:
        minEval = 100000
        bestMove = 0
        for collumn in range(getBoardInfo.sizeX):
            newBoard = makeAMove(board, collumn, 3-botNumber)
            if newBoard == False:
                continue
            hashBoard = getBoardInfo.getHashFromBoard(newBoard)
            if hashBoard in storage:
                evaluation = storage[hashBoard]
            else:
                evaluation, _, storage = minimax(newBoard, depth - 1, alpha, beta, True, botNumber, storage, heightMultiplier / 1.5)
                storage[hashBoard] = evaluation
            if (evaluation < minEval):
                minEval = evaluation
                bestMove = collumn
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval, bestMove, storage
    
