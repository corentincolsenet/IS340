from constants import WIDTH, HEIGHT, LINE_WIDTH, WIN_LINE_WIDTH, BOARD_ROWS, BOARD_COLUMNS, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, CROSS_WIDTH, SPACE, LINE_COLOR, CIRCLE_COLOR, CROSS_COLOR
import pygame, sys
import numpy as np

def draw_vertical_winning_line(screen, column, player):
	posX = column * SQUARE_SIZE + SQUARE_SIZE // 2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)

def draw_horizontal_winning_line(screen, row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)

def draw_lines(screen):
	# First horizontal line
	pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
	# Second horizontal line
	pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

	# First vertical line
	pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
	# Second vertical line
	pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures(screen, board):
	for row in range(BOARD_ROWS):
		for column in range(BOARD_COLUMNS):
			if board[row][column] == 1:
				pygame.draw.circle(screen, CIRCLE_COLOR, (int(column * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
			elif board[row][column] == 2:
				pygame.draw.line(screen, CROSS_COLOR, (column * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)	
				pygame.draw.line(screen, CROSS_COLOR, (column * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def draw_diagonal_from_up_to_down(screen, player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)

def draw_diagonal_from_down_to_up(screen, player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)