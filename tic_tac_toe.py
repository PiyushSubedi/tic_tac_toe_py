# A game called Tic - Tac - Toe
# Rule : if you have '3' of your elements in a row, columns or across a diagonal, you win

# TODO :
#   Input validation
#   Error handling
#   Support for BOT_LEVEL_HARD
#   Proper UI

import os, random, msvcrt

class Tic_Tac_Toe:
    
    NOT_ASSIGNED = 'NA'

    DEFAULT_GRID_SIZE = 3

    BOT_LEVEL_EASY = 'Easy',
    BOT_LEVEL_HARD = 'Hard'
    
    def __init__(self):
        self.__BOT_LEVEL = None
        self.__players = []
        self.__gridSize = self.DEFAULT_GRID_SIZE

    def setGridSize(self,size):
        self.__gridSize = size

    def __initializeGrid(self):
        # Method sets up a new grid
        os.system('cls')

        if self.__gridSize is None:
            self.__gridSize = DEFAULT_GRID_SIZE

        self.__grid = []
        for i in range(0,self.__gridSize):
            column = []
            for j in range(0,self.__gridSize):
                column.append(self.NOT_ASSIGNED)
            self.__grid.append(column)

        self.__drawGrid()

    def __drawGrid(self):
        # Method to draw grid for the game
        self.__gridString = ""
        for i in range(1,self.__gridSize * self.__gridSize + 1):
            self.__gridString += "_" + str(i) + "_|";
            if i % 3 == 0:
                self.__gridString += "\n"
        print(self.__gridString)

    def __addPlayer(self, name, shape, isBot):
        player = Player(name, str(len(self.__players) + 1), shape, isBot) 
        self.__players.append(player)

    def __setPlayers(self):
        choice = int(input("1. Vs Computer \n2. Vs Human\n"))
        self.__multiplayer = choice == 2

        name = input("Please enter a name for player 1 : ")
        self.__addPlayer(name, 'X', False)
        if self.__multiplayer:
            name = input("Please enter a name for player 2 : ")    
            self.__addPlayer(name, 'O', False)
        else:
            self.__addPlayer("BOT", 'O', True)

        # displaying info
        for player in self.__players:
            print(player.name + ' is ' + player.getShape() )

    def __drawShape(self, position):
        # Method registers current user's shape in the grid
        # It checks if the position is valid before registering
    
        self.__setShapeToGridAt(position.gridPosition)

        # updating grid status
        self.__grid[position.row][position.col] = self.__player.identifier;

    def __setShapeToGridAt(self, pos):
        # Method to add the shape of the current user to the grid at the given position
        os.system('cls')

        self.__gridString = self.__gridString.replace(str(pos), self.__player.getShape())
        print(self.__gridString)

    def __checkVictory(self):
        # Method validates the grid to check if victory has been reached
        if self.__player is None:
            print("player not set")
            return False

        winPattern = self.__player.identifier * self.__gridSize

        for row in range(self.__gridSize):
            resRow = resCol = ""
            for col in range(self.__gridSize):
                resRow = resRow + self.__grid[row][col]
                resCol = resCol + self.__grid[col][row]

            if resRow == winPattern or resCol == winPattern:
                return True

        resLDiag = resRDiag = ""
        for pos in range(self.__gridSize):
            resLDiag = resLDiag + self.__grid[pos][pos]
            resRDiag = resRDiag + self.__grid[pos][self.__gridSize - 1 - pos]

            if resLDiag == winPattern or resRDiag == winPattern:
                return True

        return False

    def __getBotPosition(self):
        # Returns bot's next position
        # The profitability(for bot) of the position bot choses depends on the bot level
        # For Easy mode, Bot just generates a random position
        # TODO : For higher difficulty levels

        position = None

        if self.__BOT_LEVEL is None:
            self.__BOT_LEVEL = self.BOT_LEVEL_EASY

        if self.__BOT_LEVEL == self.BOT_LEVEL_EASY:       
            emptyCells = self.__getEmptyCells()
            pos = random.sample(emptyCells, 1)[0]
            position = Position(pos, self.__gridSize)
            return position

    def __getEmptyCells(self):
        emptyCells = []
        for i in range(self.__gridSize):
            for j in range(self.__gridSize):
                if self.__grid[i][j] == self.NOT_ASSIGNED:
                    position = i * 3 + (j + 1)
                    emptyCells.append(position)
        return emptyCells

    def __isPositionValid(self, position):
        if self.__grid[position.row][position.col] != self.NOT_ASSIGNED:
            print("Position not vacant! Encroachment not allowed!")
            return False
        return True

    def start(self):

        os.system('cls')
        self.__setPlayers()

        print("Press any key to start the game")
        msvcrt.getch()

        self.__initializeGrid()

        i = 0   # Always starting with the player who registered first , TODO : Could be random

        for move in range(self.__gridSize * self.__gridSize):
            self.__player = self.__players[i]

            position = None
            if self.__player.isBot:
                position = self.__getBotPosition()
            else:
                isInputInValid = True
                while isInputInValid:
                    ## player sets the position to place their shape ##
                    pos = int(input( self.__player.name + ", please enter position to place your element : "))
                    position = Position(pos, self.__gridSize)
                    isInputInValid = not self.__isPositionValid(position)                    

            self.__drawShape(position)

            if self.__checkVictory():
                print(self.__player.name + " wins!! Bravo")
                return

            i = i ^ 1   # flipping logic

        print("Game draw! This is what happens when geniuses compete")

class Position:

    def __init__(self, pos, gridSize):
        self.gridPosition = pos
        self.row = int((pos-1) / gridSize)
        self.col = (pos-1) % gridSize

class Player:

    def __init__(self, name, identifier, shape, isBot):
        self.name = name
        self.identifier = identifier
        self.__shape = shape
        self.isBot = isBot

    def getShape(self):
        return self.__shape

    def setShape(self, shape):
        self.__shape = shape


## INITIALIZER
game = Tic_Tac_Toe()
game.start()