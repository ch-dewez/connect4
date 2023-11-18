from game import Game
import getBoardInfo
import algorithm
import copy
import time

game = Game()
player = 1
bot = 2

a = [[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55]]
for b in reversed(a):
    print([str(c).zfill(2) for c in b])

while True:
    game.print_board()
    move = int(input("collumn : "))
    game.move(move)
    


# while True:
#     while True:
#         try:
#             collumn = int(input("Enter collumn: "))
#             break
#         except ValueError:
#             print("Invalid input")
#             continue
        
#     newBoard, success = game.move(collumn)
#     if not success:
#         print("Invalid collumn")
#         continue
    
#     game.board = newBoard
#     game.print_board() 
    
#     if getBoardInfo.checkWinFullBoard(game.board, player)[0]:
#         print("You Win")
#         break
#     elif getBoardInfo.checkDraw(game.board):
#         print("Draw")
#         break
#     start = time.perf_counter()
#     _, move, _ = algorithm.minimax(copy.deepcopy(game.board), 6, -100000, 100000, True, bot)
#     end = time.perf_counter()
#     print(f"Time taken: {end - start}")
#     print(f"Bot move: {move}")
#     newBoard, _ = game.move(move)
    
#     game.board = newBoard
#     game.print_board() 
    
#     if getBoardInfo.checkWinFullBoard(game.board, bot)[0]:
#         print("You Loose")
#         break
#     elif getBoardInfo.checkDraw(game.board):
#         print("Draw")
#         break
