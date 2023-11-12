from game import Game
import getBoardInfo
import copy
import time
import algorithm

game = Game()
player = 1
bot = 2
while True:
    start = time.perf_counter()
    _, move, _ = algorithm.minimax(copy.deepcopy(game.board), 6, -100000, 100000, True, bot)
    end = time.perf_counter()
    print(f"Time taken: {end - start}")
    print(f"Bot move: {move}")
    newBoard, _ = game.move(move)
    
    game.board = newBoard
    game.print_board()
    
    if getBoardInfo.checkWinFullBoard(game.board, player)[0]:
        print("algoritm To compare won")
        break
    elif getBoardInfo.checkDraw(game.board):
        print("Draw")
        break
    start = time.perf_counter()
    _, move, _ = algorithm.minimax(copy.deepcopy(game.board), 6, -100000, 100000, True, bot)
    end = time.perf_counter()
    print(f"Time taken: {end - start}")
    print(f"Bot move: {move}")
    newBoard, _ = game.move(move)
    
    game.board = newBoard
    game.print_board()
    
    if getBoardInfo.checkWinFullBoard(game.board, bot)[0]:
        print("base algorithm won")
        break
    elif getBoardInfo.checkDraw(game.board):
        print("Draw")
        break
