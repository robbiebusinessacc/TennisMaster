import random
import time
import pygame
class Menu():
	def __init__(screen,screen_height_and_width):
		self.screen=screen
		self.screen_height_and_width=screen_height_and_width
		self.imagesDirectory="images/"
	def powerUpSelection(self):
		screen=self.screen
		screen_height_and_width=self.screen_height_and_width
		with open("score.txt","r") as scoreFile:
			scoreText=scoreFile.read()
		highScore=max(Menu.Convert_To_List(self,scoreText))
		print(highScore,'<---')
		clear = pygame.image.load(self.imagesDirectory+"whiteImage.png")
		screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
		if highScore<20:
			powerUpSelection = pygame.image.load(self.imagesDirectory+"powerUp-1.png")
		elif highScore<30 and highScore>=20:
			powerUpSelection = pygame.image.load(self.imagesDirectory+"powerUp-2.png")
		elif highScore<40 and highScore>=30:
			powerUpSelection = pygame.image.load(self.imagesDirectory+"powerUp-3.png")
		elif highScore<60 and highScore>=40:
			powerUpSelection = pygame.image.load(self.imagesDirectory+"powerUp-4.png")
		elif highScore>=60 or highScore==60:
			powerUpSelection = pygame.image.load(self.imagesDirectory+"powerUp-5.png")
		
		screen.blit(pygame.transform.scale(powerUpSelection,(screen_height_and_width,screen_height_and_width)), (0, 0))
		pygame.display.update()
		working=True
		while working:
			for event in pygame.event.get():  
				if event.type == pygame.KEYDOWN:
					if event.key==49:#49 for 1
						print("scoreBoost")
						return("scoreBoost")
					elif event.key==50 and highScore>=15:#50 for 2
						print("biggerHitbox")
						return("biggerHitbox")
					elif event.key==51 and highScore>=25:#51 for 3
						print("ballSlow")
						return("ballSlow")
					elif event.key==52 and highScore>=35:#51 for 3
						print("directionHint")
						return("directionHint")
					elif event.key==53 and highScore>=50:#51 for 3
						print("extraLife")
						return("extraLife")
					else:
						print("fail")
				elif event.type == pygame.QUIT:
						pygame.quit()
						exit()

		#bigger hitbox
		#slow down
		#extra life
		# score boost   every 5 balls you gain an extra point
		#direction hint
		#if you get a highscore of 75 you have an option to level up a power boost
		
	def mapSelection(self,screen,screen_height_and_width):
		screen=self.screen
		screen_height_and_width=self.screen_height_and_width
		with open("score.txt","r") as scoreFile:
			scoreText=scoreFile.read()
		totalScore=int(Menu.totalScores(Menu.Convert_To_List(self,scoreText)))
		clear = pygame.image.load(self.imagesDirectory+"whiteImage.png")
		screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
		if totalScore<250:
			mapSelectionBG = pygame.image.load(self.imagesDirectory+"mapselection-1.png")
		elif totalScore<500:
			mapSelectionBG = pygame.image.load(self.imagesDirectory+"mapselection-2.png")
		else:
			mapSelectionBG = pygame.image.load(self.imagesDirectory+"mapselection-3.png")

		screen.blit(pygame.transform.scale(mapSelectionBG,(screen_height_and_width,screen_height_and_width)), (0, 0))
		pygame.display.update()
		working=True
		while working:
			for event in pygame.event.get():  
				if event.type == pygame.KEYDOWN:
					totalScore=int(totalScore)
					print(totalScore,"\n",event.key)
					if event.key==49:#49 for 1
						print("test map 1")
						return("map1")
					elif event.key==50 and totalScore>=250:#50 for 2
						print("test map 2")
						return("map2")
					elif event.key==51 and totalScore>=500:#51 for 3
						print("test map 3")
						return("map3")
					else:
						print("failed")
				elif event.type == pygame.QUIT:
						pygame.quit()
						exit()
	def Convert_To_List(self, scoreText):
		newList=[]
		eachScore=""
		for letter in list(scoreText):
			if letter == ",":
				if eachScore!="":
					newList.append(int(eachScore))
				eachScore=""
			else:
				eachScore=eachScore+str(int(letter))
		return(newList)
	def totalScores(scoreFile):
		totalScoreNumber=0
		for number in scoreFile:
			if number!=1:
				totalScoreNumber+=number
		return(totalScoreNumber)
	def startAnimation(self,screen,screen_height_and_width):
		screen=self.screen
		screen_height_and_width=self.screen_height_and_width
		bg = pygame.image.load(self.imagesDirectory+"startAnimation.png")
		screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
		working=0
		pygame.display.update()
		while working==0:
			for event in pygame.event.get():

				if event.type == pygame.KEYDOWN:
					print("key hit")
					working=1
				elif event.type == pygame.QUIT:
					pygame.quit()
					exit()
