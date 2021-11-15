import random
import time
import pygame
import Menu
from RunningGame import *
class TennisMaster(RunningGame):
	def __init__(self):
		self.screen_height_and_width=TennisMaster.sizeCheck()
		self.imagesDirectory="images/"
		self.screen=pygame.display.set_mode((self.screen_height_and_width,self.screen_height_and_width))
		TennisMaster.setUp(self)
	def setUp(self):
		screen=self.screen
		screen_height_and_width=self.screen_height_and_width
		pygame.font.init()
		
		screen.fill((255,255,255))
		Menu.startAnimation(self,screen,screen_height_and_width)

		TennisMaster.clearBackground(self)
		map=Menu.mapSelection(self,screen,screen_height_and_width)
		print(str(map)+".png <====")

		bg = pygame.image.load(self.imagesDirectory+str(map)+".png")
		screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
		pygame.display.update()
		powerUps=Menu.powerUpSelection(self)
		score=0
		RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)

	def clearBackground(self):
		screen=self.screen
		screen_height_and_width=self.screen_height_and_width
		bg = pygame.image.load(self.imagesDirectory+"whiteImage.png")
		screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
		pygame.display.update()
	def sizeCheck():
		return(800)
TennisMaster()
