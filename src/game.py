from tarfile import BLOCKSIZE
from player import Player
import pygame as pygame
import random

DEFAULT_ROWS = 3
DEFAULT_COLUMNS = 3
DEFAULT_GRID_CHARACTER = 'FREE'
BLOCKSIZE = 200

class Game:
    # Define the number of rows on the grid
    rows: 0
    
    # Define the number of columns in the grid
    columns: 0
    
    # The grid for the game
    grid: list()
    
    # First player
    player_1 = {}

    # Second player    
    player_2 = {}
    
    screen = {}
    
    clock = {}

    def __init__(self, player_1, player_2):
        self.rows = DEFAULT_ROWS
        self.columns = DEFAULT_COLUMNS
        self.grid = list()
        
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1.setCharacter('O')
        self.player_2.setCharacter('X')
        self.initGrid()
        self.screen = pygame.display.set_mode((1000, 1000))
        self.clock = pygame.time.Clock()
        self.test()
    
    def test(self):
        pygame.init()
        self.screen.fill((245, 245, 220))

        while True:
            self.drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #sys.exit()
            pygame.display.update()
    
    def drawGrid(self):
        for x in range(0, self.columns, BLOCKSIZE):
            for y in range(0, self.rows, BLOCKSIZE):
                rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
    
    # Init grid and put the DEFAULT_GRID_CHARACTER for each position
    def initGrid(self):
        for i in range(0, self.columns):
            self.grid.append([i]);
            for j in range(0, self.rows):
                newCol = [j];
                self.grid[i].append(newCol);
                self.grid[i][j] = DEFAULT_GRID_CHARACTER;
            self.grid[i].pop()
    
    # Determine who will play first
    def initPlayersTurn(self):
        rand_number = random.randint(0, 100);
        
        if rand_number % 2 == 0:
            self.player_2.setTurnToPlay(True)

        self.player_1.setTurnToPlay(True)
    
    # Check if a player win by testing all the possibilities on the grid    
    def checkWin(self, player):
        player_character = player.getCharacter(); 
        
        if self.checkAllRows(player_character) == True:
            return True
        if self.checkAllColumns(player_character) == True:
            return True
        if self.checkDiagonals(player_character) == True:
            return True
        return False
    
    # Check if the player win in any of the rows
    def checkAllRows(self, player_character):
        for i in range(0, self.rows):
            if self.checkRow(i, player_character) == True:
                return True
        return False
    
    # Check if the player win in any of the columns
    def checkAllColumns(self, player_character):
        for i in range(0, self.columns):
            if self.checkColumn(i, player_character) == True:
                return True
        return False
    
    def checkDiagonals(self, player_character):
        if self.checkFirstDiagonal(player_character) == True:
            return True
        if self.checkLastDiagonal(player_character) == True:
            return True
        return False
    
    # Check if the player win on a specific row
    def checkRow(self, row, player_character, count = 0):
        if self.grid[row][count] == player_character and count < self.columns - 1:
            return self.checkRow(row, player_character, count + 1)
        if count == self.columns - 1:
            return True
        return False;
    
    # Check if the player win on a specific column
    def checkColumn(self, column, player_character, count = 0):
        if self.grid[count][column] == player_character and count < self.rows - 1:
            return self.checkRow(column, player_character, count + 1)
        if count == self.rows - 1:
            return True
        return False;
    
    # Maybe find something more generic to check the diagonals
    # Check the first diagonal of the grid (left to right)
    def checkFirstDiagonal(self, player_character, count = 0):
        if self.grid[count][count] == player_character and count < self.rows - 1:
            return self.checkFirstDiagonal(player_character, count + 1)
        if count == self.rows - 1:
            return True
        return False;
    
    # Check the second diagonal of the grid (right to left)
    def checkLastDiagonal(self, player_character, count = DEFAULT_COLUMNS - 1):
        if self.grid[count][count] == player_character and count > 0:
            return self.checkLastDiagonal(player_character, count - 1)
        if count == 0:
            return True
        return False;
    
    def getPlayerTwo(self):
        return self.player_1;
    
    def setPlayerOne(self, player_1):
        self.player_1 = player_1;
    
    def getPlayerTwo(self):
        return self.player_2;
    
    def setPlayerTwo(self, player_2):
        self.player_2 = player_2;
    
    # Return an array with the two players
    def getAllPlayers(self):
        return [self.player_1, self.player_2]
    
    def getGrid(self):
        return self.grid