from sys import argv
from draw import draw_lines, draw_figures
from win import win_condition
from constants import WIDTH, HEIGHT, BOARD_ROWS, BOARD_COLUMNS, SQUARE_SIZE, BG_COLOR
import pygame, sys
import numpy as np

pygame.init()

# screen init
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe group project')
screen.fill(BG_COLOR)

# console board with numpy
board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))

def square_clicked(row, column, player):
	board[row][column] = player

def available_square(row, column):
	return board[row][column] == 0

def is_board_full():
	for row in range(BOARD_ROWS):
		for column in range(BOARD_COLUMNS):
			if board[row][column] == 0:
				return False

	return True

def restart():
	screen.fill(BG_COLOR)
	draw_lines(screen)
	for row in range(BOARD_ROWS):
		for column in range(BOARD_COLUMNS):
			board[row][column] = 0

def main():
    draw_lines(screen)
    player = 1
    game_over = False

    # gaming loop
    while True:
        for event in pygame.event.get():
            # first exit condition
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_column = int(mouseX // SQUARE_SIZE)

                if available_square(clicked_row, clicked_column):
                    square_clicked(clicked_row, clicked_column, player)
                    if win_condition(screen, board, player):
                        game_over = True
                    player = player % 2 + 1
                    draw_figures(screen, board)

            if event.type == pygame.KEYDOWN:
                # restart condition
                if event.key == pygame.K_r:
                    restart()
                    player = 1
                    game_over = False
                # second exit condition (when q is pressed)
                if event.key == pygame.K_q:
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    sys.exit(main())