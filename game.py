from termcolor import colored
class Game:
    def __init__(self, sizeX=7, sizeY=6):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = [0, 0]
        self.sizeBoard = 56
        self.playerToMove = 1
    
    def print_board(self):
        boardToPrint = [[0 for x in range(self.sizeX)] for y in range(self.sizeY)]
        
        for j, playerBoard in enumerate(self.board):
            for i, bit in enumerate(bin(playerBoard)[2:].zfill(self.sizeBoard)):
                if bit == "1":
                    y = (i // (self.sizeX + 1)) - 1
                    x = i % (self.sizeX + 1)
                    boardToPrint[y][x] = j + 1
        
        for y in range(self.sizeY):
            print("  ".join(colored("X", "red") if e == 1 else colored("Y", "yellow") if e == 2 else "O" for e in boardToPrint[y]))
        print()

    def changePlayerPlaying(self):
        self.playerToMove = 3 - self.playerToMove

    def move(self, collumn):
        
        maskForOneRow = 1 << self.sizeY + 1 - collumn # + 1 -> one collumn for easier comparaison
        mask = maskForOneRow | maskForOneRow << (self.sizeY + 2) | maskForOneRow << ((self.sizeY + 2) * 2) | maskForOneRow << ((self.sizeY + 2) * 3) | maskForOneRow << ((self.sizeY + 2) * 4) | maskForOneRow << ((self.sizeY + 2) * 5)
        height = bin((self.board[0] & mask) | ( self.board[1] & mask)).count("1")
        if height == self.sizeY:
            return False
        
        boardMove = 1 << (self.sizeX + 1) * height + self.sizeX - collumn
        self.board[self.playerToMove-1] |= boardMove
        self.changePlayerPlaying()
        return True
        