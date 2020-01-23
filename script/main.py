class Board:
    class Piece:
        display = " "
        def __init__(self, display):
            self.display = display
        def __str__(self):
            if self.display == None:
                return " "
            return self.display

    sizeX = 4
    sizeY = 4
    sizeZ = 4
    field = None
    def __init__(self):
        self.field = []
        for i in range(0, self.sizeX):
            self.field.append([])
            for j in range(0, self.sizeY):
                self.field[i].append([])
                for k in range(0, self.sizeZ):
                    self.field[i][j].append(self.Piece(None))

    def __str__(self):
        print("#  #  #  #  #  #", end="  |  ")
        print("#  #  #  #  #  #", end="  |  ")
        print("#  #  #  #  #  #", end="  |  ")
        print("#  #  #  #  #  #", end="\n")
        for i in range(0, self.sizeX):
            for j in range(0, self.sizeY):
                print("#", end="  ")
                for k in range(0, self.sizeZ):
                    print("{}".format(self.field[i][j][k]), end="  ")
                if j != self.sizeY-1:
                    print("#", end="  |  ")
                else:
                    print("#")
        print("#  #  #  #  #  #", end="  |  ")
        print("#  #  #  #  #  #", end="  |  ")
        print("#  #  #  #  #  #", end="  |  ")
        print("#  #  #  #  #  #", end="")
        return ""

# ENTRY
board = Board()
print(board)