import pygame
from pytmx import load_pygame
from data.scripts.settings import TILESIZE
from data.scripts.tile import Tile

class Level_1():

	def __init__(self, surface, tile_rects):
		self.display = surface
		self.tile_rects = tile_rects
		self.tmx_data = load_pygame('data/levels/level_1.tmx')
		self.terrain = self.tmx_data.get_layer_by_name('terrain')
		self.coins = self.tmx_data.get_layer_by_name('coins')
		self.grass = self.tmx_data.get_layer_by_name('grass')
		self.rocks = self.tmx_data.get_layer_by_name('rocks')

	# loads terrain layer ----------------------------------
	def load_terrain(self):
		for x, y, surf in self.terrain.tiles():
			self.tile = Tile(surf, (x * TILESIZE, y * TILESIZE))
			self.tile_rects.append(self.tile.rect)
			self.display.blit(self.tile.image, self.tile.position)	

	# loads coins layer ------------------------------------
	def load_coins(self):
		for x, y, surf in self.coins.tiles():
			self.tile = Tile(surf, (x * TILESIZE, y * TILESIZE))
			self.tile_rects.append(self.tile.rect)	
			self.display.blit(self.tile.image, self.tile.position)			

	# loads grass layer ------------------------------------
	def load_grass(self):
		for x, y, surf in self.grass.tiles():
			self.tile = Tile(surf, (x * TILESIZE, y * TILESIZE))
			self.tile_rects.append(self.tile.rect)	
			self.display.blit(self.tile.image, self.tile.position)		

	# loads rocks layer ------------------------------------
	def load_rocks(self):
		for x, y, surf in self.rocks.tiles():
			self.tile = Tile(surf, (x * TILESIZE, y * TILESIZE))
			self.tile_rects.append(self.tile.rect)
			self.display.blit(self.tile.image, self.tile.position)				

	def run(self):
		# runs level 1 -------------------------------------
		self.load_terrain()
		self.load_rocks()
		self.load_grass()
		self.load_coins()

