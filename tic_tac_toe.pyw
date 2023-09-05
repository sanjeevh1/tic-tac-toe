import pygame
import sys
from board import Board
import game_functions
from settings import Settings

black = (0, 0, 0)
red = (255, 0, 0)

pygame.init()
s = Settings()
screen_width = 2 * s.margin + 3 * s.box_width
screen = pygame.display.set_mode((screen_width, screen_width))
screen.fill(s.bg_color)
board = Board()

#draws lines between squares
pygame.draw.line(screen, s.grid_color, (s.margin + s.box_width, s.margin), (s.margin + s.box_width, screen_width - s.margin), s.line_width)
pygame.draw.line(screen, s.grid_color, (s.margin + 2 * s.box_width, s.margin), (s.margin + 2 * s.box_width, screen_width - s.margin), s.line_width)
pygame.draw.line(screen, s.grid_color, (s.margin, s.margin + s.box_width), (screen_width - s.margin, s.margin + s.box_width), s.line_width)
pygame.draw.line(screen, s.grid_color, (s.margin, s.margin + 2 * s.box_width), (screen_width - s.margin, s.margin + 2 * s.box_width), s.line_width)
 
player = "X"
while True:
	pygame.display.flip()
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
			
		if board.get_winner() == None:
			if event.type == pygame.MOUSEBUTTONUP:
				x, y = pygame.mouse.get_pos()
				row, col = game_functions.get_spot(s, x, y)
				
				if board.grid[row][col] == '':
					game_functions.draw_letter(s, screen, player, row, col)
					board.grid[row][col] = player
					
					#changes players
					if player == "X":
						player = "O"
					else:
						player = "X"
						
		if board.get_winner() != None:
			game_functions.end_game(s, screen, board)
