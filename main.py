from game import Game
import getBoardInfo
import algorithm
import copy
import time

game = Game()
player = 1
bot = 2
while True:
    game.print_board()
    while True:
        try:
            collumn = int(input("Enter collumn: "))
            break
        except ValueError:
            print("Invalid input")
            continue
        
    newBoard, success = game.move(collumn)
    if not success:
        print("Invalid collumn")
        continue
    
    game.board = newBoard
    
    if getBoardInfo.checkWinFullBoard(game.board, player)[0]:
        print("You Win")
        break
    elif getBoardInfo.checkDraw(game.board):
        print("Draw")
        break
    start = time.perf_counter()
    _, move = algorithm.minimax(copy.deepcopy(game.board), 6, -100000, 100000, True, bot)
    end = time.perf_counter()
    print(f"Time taken: {end - start}")
    print(f"Bot move: {move}")
    newBoard, _ = game.move(move)
    
    game.board = newBoard
    
    if getBoardInfo.checkWinFullBoard(game.board, bot)[0]:
        print("You Loose")
        break
    elif getBoardInfo.checkDraw(game.board):
        print("Draw")
        break
