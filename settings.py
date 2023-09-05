import pygame
class Settings():
	
	def __init__(self):
		self.box_width = 170
		self.margin = 10
		self.line_width = 5
		self.big_font = pygame.font.Font('freesansbold.ttf', 150)
		self.small_font = pygame.font.Font('freesansbold.ttf', 50)
		
		self.bg_color = (255, 255, 255)
		self.font_color = (0, 0, 0)
		self.grid_color = (0, 0, 0)
		self.ending_color = (255, 0, 0)  
		
