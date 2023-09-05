"""A module to draw letters and lines on the screen."""
import pygame

def get_spot(s, x, y):
	"""Returns the spot corresponding to coordinates (x,y)."""
	if x < s.margin + s.box_width:
		row = 0
	elif x < s.margin + 2 * s.box_width:
		row = 1
	else:
		row = 2
	if y < s.margin + s.box_width:
		col = 0
	elif y < s.margin + 2 * s.box_width:
		col = 1
	else:
		col = 2
	return row, col
	
def get_coordinates(s, row, col):
	"""Returns the coordinates of the center of spot (row, col)."""
	a = (s.margin + s.box_width) / 2 + s.box_width * row
	b = (s.margin + s.box_width) / 2 + s.box_width * col
	return a, b
	
def draw_letter(s, screen, letter, row, col):
	"""Draws the given letter in the spot (row, col)."""
	text = s.big_font.render(letter.title(), True, s.font_color)
	point = get_coordinates(s, row, col)
	text_rect = text.get_rect(center=point)
	screen.blit(text, text_rect)

def end_game(s, screen, board):
	"""Displays winner and line showing winning row."""
	if board.get_winner() == 'draw':
				string = 'DRAW'
				
	else:
		string = board.get_winner() + " WINS!"
		#draws a line across the winning row
		a, b = board.winning_row[0]
		c, d = board.winning_row[1]
		p1 = get_coordinates(s, a, b)
		p2 = get_coordinates(s, c, d)
		pygame.draw.line(screen, s.ending_color, p1, p2, s.line_width)
	
	#displays winner of game
	
	text = s.small_font.render(string, True, s.ending_color)
	width, height = s.small_font.size(string)
	
	x, y = screen.get_size()	
	x /= 2
	y /= 2
	text_rect = text.get_rect(center=(x,y))
	screen.blit(text, text_rect)
