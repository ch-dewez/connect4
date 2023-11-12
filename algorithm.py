from copy import deepcopy, copy
import getBoardInfo


def minimax(board, depth, alpha, beta, maximizingPlayer, botNumber):
    if depth == 0 or getBoardInfo.isFinished(board):
        return getBoardInfo.getBoardEval(board, botNumber), 0

    if maximizingPlayer:
        maxEval = -100000
        bestMove = 0
        for collumn in range(7):
            newBoard = deepcopy(board)
            if (board[0][collumn] != 0):
                continue
            for y in reversed(range(getBoardInfo.sizeY)):
                if (board[y][collumn] == 0):
                    newBoard[y][collumn] = botNumber
                    break
            evaluation, _ = minimax(deepcopy(newBoard), depth - 1, alpha, beta, False, botNumber)
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
        for collumn in range(7):
            newBoard = deepcopy(board)
            if (board[0][collumn] != 0):
                continue
            for y in reversed(range(getBoardInfo.sizeY)):
                if (board[y][collumn] == 0):
                    newBoard[y][collumn] = 3 - botNumber
                    break
            evaluation, _ = minimax(deepcopy(newBoard), depth - 1, alpha, beta, True, botNumber)
            if (evaluation < minEval):
                minEval = evaluation
                bestMove = collumn
            beta = min(beta, minEval)
            if beta <= alpha:
                break
        return minEval, bestMove