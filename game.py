from termcolor import colored
class Game:
    def __init__(self, sizeX=7, sizeY=6):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = self.new_board() # 1 = X; 2 = Y
        self.playerToMove = 1

    def new_board(self):
        newBoard = []
        for y in range(self.sizeY):
            newBoard.append([])
            for x in range(self.sizeX):
                newBoard[y].append(0)
        return newBoard
    
    def print_board(self):
        for y in range(self.sizeY):
            print("  ".join(colored("X", "red") if e == 1 else colored("Y", "yellow") if e == 2 else "O" for e in self.board[y]))
        print()

    def changePlayerPlaying(self):
        self.playerToMove = 3 - self.playerToMove

    def move(self, collumn, doChangePlayerPlaying = True):
        newBoard = self.board.copy()
        if (self.board[0][collumn] != 0):
            return ([], False)
        for y in reversed(range(self.sizeY)):
            if (self.board[y][collumn] == 0):
                newBoard[y][collumn] = self.playerToMove
                if (doChangePlayerPlaying): self.changePlayerPlaying()
                return  (newBoard, True)