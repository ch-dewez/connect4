from game import Game
import getBoardInfo
import algorithm

game = Game()
# a full board
game.playerToMove = 1 if input("Do you want to start ? (y/n) ") == "y" else 2
humanPlayer = 1
bot = 2


def humanToMove():
    
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
        return humanToMove()
    print(f"eval {getBoardInfo.getBoardEval(game.board, humanPlayer)}")
    game.print_board()
    
    if getBoardInfo.checkWin(game.board, humanPlayer):
        return "human win"
    elif getBoardInfo.checkDraw(game.board):
        return "draw"

    return "success"

def botToMove():
    _, move, storage = algorithm.minimax(game.board, 10, -100000, 100000, True, bot)
    print(f"Bot move: {move}")
    
    _ = game.move(move)
    
    game.print_board() 
    
    if getBoardInfo.checkWin(game.board, bot):
        return "bot win"
    elif getBoardInfo.checkDraw(game.board):
        return "draw"
    

while True:
    if game.playerToMove == humanPlayer:
        result = humanToMove()
        if result == "human win":
            print("You win")
            break
        elif result == "draw":
            print("draw")
            break
        
    if game.playerToMove == bot:
        result = botToMove()
        if result == "bot win":
            print("You Loose")
            break
        elif result == "draw":
            print("draw")
            break
        
    
