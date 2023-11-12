from game import Game

game = Game()
game.print_board()
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
        
    newBoard, success = game.move(collumn)
    if not success:
        print("Invalid collumn")
        continue