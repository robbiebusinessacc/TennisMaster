import random
import time
import pygame
import TennisMaster #if i have this it breaks
from Menu import *
class RunningGame:
	def __init__(direction,screen,screen_height_and_width,score,map,powerUps):
		self.direction=direction
		self.screen=screen
		self.screen_height_and_width=screen_height_and_width
		self.score=score
		self.map=map 
		self.powerUps=powerUps
	def imagesDirectory():
		return("images/")
	def tennisBall(direction,screen,screen_height_and_width,score,map,powerUps):
		backwards=False
		working=True
		slowdown=0
		speed=12-slowdown+score*0.5
		speed=int(speed)
		if powerUps=="scoreBoost" and speed%4==0:
			score+=1
		elif powerUps=="ballSlow":
			slowdown=2
		score+=1
		if powerUps=="biggerHitbox":
			biggerHitbox=True
		else:
			biggerHitbox=False
		if direction=="left":
			x=int(screen_height_and_width/160)
			y=int(screen_height_and_width/2-int(screen_height_and_width/22))
			ball = pygame.image.load(RunningGame.imagesDirectory()+"tennisball.png")
			clear = pygame.image.load(RunningGame.imagesDirectory()+"whiteImage.png")
			bg = pygame.image.load(RunningGame.imagesDirectory()+str(map)+"-left.png")
			start=int(screen_height_and_width/160)
			while working:
				screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
				screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
				screen.blit(pygame.transform.scale(ball,(int(screen_height_and_width/10),int(screen_height_and_width/10))), (x,y))
				RunningGame.scoreBoard(screen,screen_height_and_width,score)
				pygame.display.update()
				time.sleep(0.005)
				x+=speed

				for event in pygame.event.get():  
					if event.type == pygame.KEYDOWN:
						if event.key==pygame.K_a or event.key==1073741904: #97 = a
							if x>200 and x<400:	
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif powerUps=="extraLife":
								powerUps=""
								time.sleep(0.5)
								print("extra life over")
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif biggerHitbox and x>150 and x<450:
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							else:
								
								RunningGame.failScreen(screen,screen_height_and_width,score)

						else:
							RunningGame.failScreen(screen,screen_height_and_width,score)
					elif event.type == pygame.QUIT:
						pygame.quit()
						exit()
					if x<screen_height_and_width/160:
						screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
						screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
						working=False
					if backwards:
						if speed>0:
							speed=(speed*-1)*2
		if direction=="right":
			x=int(screen_height_and_width-screen_height_and_width/160)
			y=int(screen_height_and_width/2-int(screen_height_and_width/22))
			ball = pygame.image.load(RunningGame.imagesDirectory()+"tennisball.png")
			clear = pygame.image.load(RunningGame.imagesDirectory()+"whiteImage.png")
			bg = pygame.image.load(RunningGame.imagesDirectory()+str(map)+"-right.png")
			start=int(screen_height_and_width/160)
			while working:
				screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
				screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))

				screen.blit(pygame.transform.scale(ball,(int(screen_height_and_width/10),int(screen_height_and_width/10))), (x,y))
				RunningGame.scoreBoard(screen,screen_height_and_width,score)
				pygame.display.update()
				time.sleep(0.005)
				x-=speed
				for event in pygame.event.get():  
					if event.type == pygame.KEYDOWN:
						if event.key==100 or event.key==1073741903:#100 = d
							if x<600 and x>400:	
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif powerUps=="extraLife":
								powerUps=""
								time.sleep(0.5)
								print("extra life over")
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif biggerHitbox and x<650 and x<350:
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							else:
								
								RunningGame.failScreen(screen,screen_height_and_width,score)
						else:
							RunningGame.failScreen(screen,screen_height_and_width,score)
					elif event.type == pygame.QUIT:
						pygame.quit()
						exit()
					if x<screen_height_and_width/160:
						screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
						screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
						working=False
					if backwards:
						if speed>0:
							speed=(speed*-1)*2

		if direction=="up":
			x=int(screen_height_and_width/2-screen_height_and_width/20)
			y=int(int(screen_height_and_width/80))
			ball = pygame.image.load(RunningGame.imagesDirectory()+"tennisball.png")
			clear = pygame.image.load(RunningGame.imagesDirectory()+"whiteImage.png")

			bg = pygame.image.load(RunningGame.imagesDirectory()+str(map)+"-up.png")
			start=int(screen_height_and_width/160)
			while working:
				screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
				screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
				screen.blit(pygame.transform.scale(ball,(int(screen_height_and_width/10),int(screen_height_and_width/10))), (x,y))
				RunningGame.scoreBoard(screen,screen_height_and_width,score)
				pygame.display.update()
				time.sleep(0.005)
				y+=speed

				for event in pygame.event.get():  
					if event.type == pygame.KEYDOWN:
						if event.key==119 or event.key == 1073741906:#199 = w
							if y>200 and y<400:	
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif powerUps=="extraLife":
								powerUps=""
								time.sleep(0.5)
								print("extra life over")
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif biggerHitbox and y>150 and y<450:
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							else:
								RunningGame.failScreen(screen,screen_height_and_width,score)
						else:
							RunningGame.failScreen(screen,screen_height_and_width,score)
					elif event.type == pygame.QUIT:
						pygame.quit()
						exit()
					if x<screen_height_and_width/160:
						screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
						screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
						working=False
					if backwards:
						if speed>0:
							speed=(speed*-1)*2
		if direction=="down":
			x=int(screen_height_and_width/2-screen_height_and_width/20)
			y=int(int(screen_height_and_width-screen_height_and_width/80))
			ball = pygame.image.load(RunningGame.imagesDirectory()+"tennisball.png")
			clear = pygame.image.load(RunningGame.imagesDirectory()+"whiteImage.png")
			bg = pygame.image.load(RunningGame.imagesDirectory()+str(map)+"-down.png")
			start=int(screen_height_and_width/160)
			while working:
				screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
				screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
				screen.blit(pygame.transform.scale(ball,(int(screen_height_and_width/10),int(screen_height_and_width/10))), (x,y))
				RunningGame.scoreBoard(screen,screen_height_and_width,score)
				pygame.display.update()
				time.sleep(0.005)
				y-=speed
				for event in pygame.event.get():  
					if event.type == pygame.KEYDOWN:
						if event.key==115 or event.key==1073741905:#115 = a
							if y<600 and y>400:	
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif powerUps=="extraLife":
								time.sleep(0.5)
								powerUps=""
								print("extra life over")
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							elif biggerHitbox and y<650 and y>350:
								backwards=True
								RunningGame.scoreBoard(screen,screen_height_and_width,score)
								RunningGame.NextBall(screen,screen_height_and_width,score,map,powerUps)
							else:
								RunningGame.failScreen(screen,screen_height_and_width,score)
						else:
							RunningGame.failScreen(screen,screen_height_and_width,score)
					elif event.type == pygame.QUIT:
							pygame.quit()
							exit()
					if x<screen_height_and_width/160:
						screen.blit(pygame.transform.scale(clear,(screen_height_and_width,screen_height_and_width)), (0, 0))
						screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
						working=False
					if backwards:
						if speed>0:
							speed=(speed*-1)*2


	def NextBall(screen,screen_height_and_width,score,map,powerUps):
		newDirection=random.randint(1,4)
		#2 and 4 dont work
		if powerUps=="directionHint":
			if newDirection==1:
				x=int(screen_height_and_width/160)
				y=int(screen_height_and_width/2-int(screen_height_and_width/22))
				arrow=pygame.image.load(RunningGame.imagesDirectory()+"leftArrow.png")
			if newDirection==2:
				x=int(screen_height_and_width-screen_height_and_width/160-82)
				y=int(screen_height_and_width/2-int(screen_height_and_width/22))
				arrow=pygame.image.load(RunningGame.imagesDirectory()+"rightArrow.png")
				print(arrow)
			if newDirection==3:
				x=int(screen_height_and_width/2-screen_height_and_width/20)
				y=int(int(screen_height_and_width/80))
				arrow=pygame.image.load(RunningGame.imagesDirectory()+"upArrow.png")
				
			if newDirection==4:
				x=int(screen_height_and_width/2-screen_height_and_width/20)
				y=int(int(screen_height_and_width-screen_height_and_width/80)-82)
				arrow=pygame.image.load(RunningGame.imagesDirectory()+"downArrow.png")
				pygame.display.update()
			screen.blit(pygame.transform.scale(arrow,(int(screen_height_and_width/10),int(screen_height_and_width/10))), (x,y))
			pygame.display.update()
			time.sleep(0.05)
		if newDirection==1:
			RunningGame.tennisBall("left",screen,screen_height_and_width,score,map,powerUps)
		elif newDirection==2:
			RunningGame.tennisBall("right",screen,screen_height_and_width,score,map,powerUps)
		
		elif newDirection==3:
			RunningGame.tennisBall("up",screen,screen_height_and_width,score,map,powerUps)

		elif newDirection==4:
			RunningGame.tennisBall("down",screen,screen_height_and_width,score,map,powerUps)
	def Convert_To_List(scoreText):
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
	def scoreBoard(screen,screen_height_and_width,score):
		if score>100000000000000000000000000000000000000000000:
			score-=100000000000000000000000000000000000000000000
			myfont = pygame.font.SysFont('Comic Sans MS', 100)
			bigfont = pygame.font.SysFont('They definitely dont have this installed Gothic', 120)
			textsurface = myfont.render(str(score), False, (0, 0, 0))
			if score>=10:
				screen.blit(textsurface,(145,270))
			else:
				screen.blit(textsurface,(179,270))
				
			with open("score.txt","r") as scoreFile:
				scoreText=scoreFile.read()
				highScore=max(RunningGame.Convert_To_List(scoreText))
				textsurface = myfont.render(''+str(highScore), False, (0, 0, 0))
				if highScore>=10:
					screen.blit(textsurface,(541,270))
				else:
					screen.blit(textsurface,(570,270))
				if highScore<score:
					textsurface = bigfont.render("New Highscore", False, (0, 0, 0))
					screen.blit(pygame.transform.scale(textsurface,(600,110)), (100, 415))
		else:
			myfont = pygame.font.SysFont('Comic Sans MS', 50)
			textsurface = myfont.render("Score: "+str(score), False, (0, 0, 0))
			if score>=10:
				screen.blit(textsurface,(10,10))
			else:
				screen.blit(textsurface,(10,10))

		
		pygame.display.update()
	def clearBackground(screen,screen_height_and_width):
		bg = pygame.image.load(RunningGame.imagesDirectory()+"whiteImage.png")
		screen.blit(pygame.transform.scale(bg,(screen_height_and_width,screen_height_and_width)), (0, 0))
		pygame.display.update()
	def failScreen(screen,screen_height_and_width,score):
		score+=100000000000000000000000000000000000000000000
		failPanel = pygame.image.load(RunningGame.imagesDirectory()+"failScreen.png")
		screen.blit(pygame.transform.scale(failPanel,(screen_height_and_width,screen_height_and_width)), (0, 0))
		
		with open("score.txt", "a") as scoreFile:
			scoreFile.write(","+str(score-100000000000000000000000000000000000000000000))
		RunningGame.scoreBoard(screen,screen_height_and_width,score)
		pygame.display.update()	
		time.sleep(2.5)
		TennisMaster.setUp()
	def totalScores(scoreFile):
		totalScoreNumber=0
		for number in scoreFile:
			if number!=1:
				totalScoreNumber+=number
		return(totalScoreNumber)
	def sizeCheck():
		'''
		sizeOptions=int(input("Pick your resolution\n1 for 1080p\n2 for 2k\n4 for 4k\n"))
		if sizeOptions==1:
			return(800)
		elif sizeOptions==2:
			return(1400)
		elif sizeOptions==4:
			return(1900)
		else:
			print("You Failed Basic Directions")
			return(1)
		'''
		return(800)