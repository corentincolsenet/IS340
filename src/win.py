from constants import BOARD_ROWS, BOARD_COLUMNS
from draw import draw_vertical_winning_line, draw_horizontal_winning_line, draw_diagonal_from_up_to_down, draw_diagonal_from_down_to_up

def win_condition(screen, board, player):
	# vertical win condition
	for column in range(BOARD_COLUMNS):
		if board[0][column] == player and board[1][column] == player and board[2][column] == player:
			draw_vertical_winning_line(screen, column, player)
			return True

	# horizontal win condition
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(screen, row, player)
			return True

	# asc diagonal win condition
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_diagonal_from_up_to_down(screen, player)
		return True

	# desc diagonal win condition
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_diagonal_from_down_to_up(screen, player)
		return True

	return False