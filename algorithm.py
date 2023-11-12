from copy import deepcopy
import getBoardInfo

#  trying to make optimization 8 -> done, 9, 2 of https://larswaechter.dev/blog/minimax-performance-improvements/#:~:text=Improving%20Minimax%20performance%201%201.%20Alpha-Beta%20Pruning%20One,8.%20Improve%20.hasPlayerWon%20%28%29%20function%20...%20%C3%89l%C3%A9ments%20suppl%C3%A9mentaires

def minimax(board, depth, alpha, beta, maximizingPlayer, botNumber, lastMove = []):
    if lastMove == []:
        if depth == 0 or getBoardInfo.isFinished(board):
            return getBoardInfo.getBoardEval(board, botNumber), 0
    else:
        if depth == 0 or getBoardInfo.isFinishedLastMove(lastMove[0], lastMove[1], botNumber if not maximizingPlayer else 3 - botNumber, board):
            return getBoardInfo.getBoardEval(board, botNumber), 0

    if maximizingPlayer:
        maxEval = -100000
        bestMove = 0
        for collumn in range(getBoardInfo.sizeX):
            newBoard = deepcopy(board)
            move = []
            if (board[0][collumn] != 0):
                continue
            for y in reversed(range(getBoardInfo.sizeY)):
                if (board[y][collumn] == 0):
                    newBoard[y][collumn] = botNumber
                    move = [collumn, y]
                    break
            evaluation, _ = minimax(deepcopy(newBoard), depth - 1, alpha, beta, False, botNumber, move)
            if (evaluation > maxEval):
                maxEval = evaluation
                bestMove = collumn
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
        return maxEval, bestMove
    else:
        minEval = 100000
        bestMove = 0
        move = []
        for collumn in range(getBoardInfo.sizeX):
            newBoard = deepcopy(board)
            if (board[0][collumn] != 0):
                continue
            for y in reversed(range(getBoardInfo.sizeY)):
                if (board[y][collumn] == 0):
                    newBoard[y][collumn] = 3 - botNumber
                    move = [collumn, y]
                    break
            evaluation, _ = minimax(deepcopy(newBoard), depth - 1, alpha, beta, True, botNumber, move)
            if (evaluation < minEval):
                minEval = evaluation
                bestMove = collumn
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval, bestMove