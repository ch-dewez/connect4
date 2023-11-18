from game import Game
import getBoardInfo
import algorithm
import copy
import time

game = Game()
player = 1
bot = 2


while True:
    while True:
        try:
            collumn = int(input("Enter collumn: "))
            break
        except ValueError:
            print("Invalid input")
            continue

    success = game.move(collumn)
    if not success:
        print("Invalid collumn")
        continue

    game.print_board()

    if getBoardInfo.checkWin(game.board, player):
        print("You Win")
        break
    elif getBoardInfo.checkDraw(game.board):
        print("Draw")
        break

    start = time.perf_counter()
    _, move, _ = algorithm.minimax(
        copy.deepcopy(game.board), 6, -100000, 100000, True, bot
    )
    end = time.perf_counter()

    print(f"Time taken: {end - start}")
    print(f"Bot move: {move}")

    _ = game.move(move)

    game.print_board()

    if getBoardInfo.checkWin(game.board, bot):
        print("You Loose")
        break
    elif getBoardInfo.checkDraw(game.board):
        print("Draw")
        break
