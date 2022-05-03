from sys import argv

from pyparsing import White
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

# clock for the game
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
toggle = False
pygame.mixer.music.load("./sounds/Coconut Mall - Mario Kart Wii [OST].mp3")
bg = pygame.image.load("./images/bg.jpeg")
wer = pygame.image.load("./images/weirdo.png")
wal = pygame.image.load("./images/watdaf2.png")
p1 = pygame.image.load("./images/p1.png")
p2 = pygame.image.load("./images/p2.png")

color_light = (170,170,170)
color_dark = (0,0,0)
smallfont = pygame.font.SysFont('freesansbold.ttf',35)
text = smallfont.render('QUIT' , True , white)

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


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH/2-75 <= mouse[0] <= WIDTH/2-75+140 and HEIGHT-80 <= mouse[1] <= HEIGHT-80+40:
                    pygame.quit()
                    sys.exit(0)
                
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        smallText = pygame.font.Font('freesansbold.ttf',32)
        mouse = pygame.mouse.get_pos()
        TextSurf, TextRect = text_objects("Tic Tac Toe", largeText)
        Instr, TextInstr = text_objects('Press enter to start', smallText)
        TextRect.center = ((WIDTH/2),(HEIGHT/9))
        TextInstr.center = ((WIDTH/2), (HEIGHT/5))
        screen.blit(TextSurf, TextRect)
        screen.blit(Instr, TextInstr)
        screen.blit(bg, (150, 150))
        screen.blit(wer, (0, 150))
        screen.blit(wal, (350, 450))
        if WIDTH/2-75 <= mouse[0] <= WIDTH/2-75+140 and HEIGHT-80 <= mouse[1] <= HEIGHT-80+40:
            pygame.draw.rect(screen,color_light,[WIDTH/2-75,HEIGHT-80,140,40])
        else:
            pygame.draw.rect(screen,color_dark,[WIDTH/2-75,HEIGHT-80,140,40])
        screen.blit(text , (WIDTH/2-35,HEIGHT-72))
        pygame.display.update()
        clock.tick(15)
    screen.fill(BG_COLOR)


def main():
    pygame.mixer.music.play(-1)
    game_intro()
    draw_lines(screen)
    player = 1
    game_over = False

    # gaming loop
    while True:
        if (player == 1 and game_over == True):
            screen.blit(p2, (0, 0))
        elif (player == 2 and game_over == True):
            screen.blit(p1, (0, 0))
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