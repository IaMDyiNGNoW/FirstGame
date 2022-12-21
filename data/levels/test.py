import pygame, sys
from pytmx import load_pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
display = pygame.Surface((300, 200))
pygame.display.set_caption('level test')

# getting the level
tmx_data = load_pygame('level_1.tmx')
terrain = tmx_data.get_layer_by_name('terrain')
coins = tmx_data.get_layer_by_name('coins')
grass = tmx_data.get_layer_by_name('grass')
rocks = tmx_data.get_layer_by_name('rocks')

def load_terrain():
	for x, y, surf in terrain.tiles():
		display.blit(surf, (x * 16, y * 16))	

def load_coins():
	for x, y, surf in coins.tiles():
		display.blit(surf, (x * 16, y * 16))	

def load_grass():
	for x, y, surf in grass.tiles():
		display.blit(surf, (x * 16, y * 16))	

def load_rocks():
	for x, y, surf in rocks.tiles():
		display.blit(surf, (x * 16, y * 16))	


# main loop
while True:

	display_surf = pygame.transform.scale(display, (600, 400))
	screen.blit(display_surf, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# game code
	display.fill('black')
	load_terrain()
	load_coins()
	load_grass()
	load_rocks()


	pygame.display.update()