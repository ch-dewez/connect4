from game import Game
import getBoardInfo
import copy
import time
import algorithm
from algorithmToCompare import algorithm as algorithmToCompare
from algorithmToCompare import getBoardInfo as getBoardInfoToCompare

def bitboardToBoard(bitboard):
    board = [[0 for x in range(7)] for y in range(6)]
    for j, playerBoard in enumerate(bitboard):
            for i, bit in enumerate(bin(playerBoard)[2:].zfill(56)):
                if bit == "1":
                    y = (i // (7 + 1)) - 1
                    x = i % (7 + 1)
                    board[y][x] = j + 1
    return board

game = Game()
player = 1
bot = 2
game.move(5)
while True:
    start = time.perf_counter()
    _, move, _ = algorithmToCompare.minimax(
        copy.deepcopy(bitboardToBoard(game.board)), 6, -100000, 100000, True, 2
    )
    end = time.perf_counter()
    print(f"Time taken: {end - start}")
    print(f"Bot move: {move}")
    game.move(move)
    
    game.print_board()

    if getBoardInfo.checkWin(game.board, player):
        print("algoritm To compare won")
        break
    elif getBoardInfoToCompare.checkDraw(bitboardToBoard(game.board)):
        print("Draw")
        break
    start = time.perf_counter()
    _, move, _ = algorithm.minimax(
        copy.deepcopy(game.board), 10, -100000, 100000, True, 1
    )
    end = time.perf_counter()
    print(f"Time taken: {end - start}")
    print(f"Bot move: {move}")
    game.move(move)
    game.print_board()

    if getBoardInfo.checkWin(game.board, bot):
        print("base algorithm won")
        break
    elif getBoardInfoToCompare.checkDraw(bitboardToBoard(game.board)):
        print("Draw")
        break
