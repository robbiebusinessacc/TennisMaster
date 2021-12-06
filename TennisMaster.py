import random
import time
import pygame
import Menu
from RunningGame import *


class TennisMaster(RunningGame):
    def __init__(
        self,
    ):
        # super(TennisMaster, self).__init__(self,direction, screen, screen_height_and_width, score, map, powerUps)
        self.screen_height_and_width = TennisMaster.sizeCheck(self)
        self.imagesDirectory = "images/"
        self.screen = pygame.display.set_mode(
            (
                self.screen_height_and_width,
                self.screen_height_and_width,
            )
        )
        TennisMaster.setUp(self)

    def setUp(
        self,
    ):
        screen = self.screen
        screen_height_and_width = self.screen_height_and_width


        pygame.display.set_caption('TennisMaster')
        icon = pygame.image.load('images/icon'+".png")
        pygame.display.set_icon(icon)
        

        pygame.font.init()

        screen.fill(
            (
                255,
                255,
                255,
            )
        )
        Menu.startAnimation(
            screen,
            screen_height_and_width,
        )

        TennisMaster.clearBackground(
            screen,
            screen_height_and_width,
        )
        level =  Menu.levelsSelection(
            screen,
            screen_height_and_width,
        )
        map = Menu.mapSelection(
            screen,
            screen_height_and_width,
        )
        print("images/" + str(map) + ".png")
        bg = pygame.image.load("images/" + str(map) + ".png")
        screen.blit(
            pygame.transform.scale(
                bg,
                (
                    screen_height_and_width,
                    screen_height_and_width,
                ),
            ),
            (
                0,
                0,
            ),
        )
        powerUps = Menu.powerUpSelection(
            screen,
            screen_height_and_width,
        )
        score = 0
        RunningGame.NextBall(
            screen,
            screen_height_and_width,
            score,
            map,
            powerUps,
            level
        )

    def clearBackground(
        screen,
        screen_height_and_width,
    ):

        bg = pygame.image.load("images/" + "whiteImage.png")
        screen.blit(
            pygame.transform.scale(
                bg,
                (
                    screen_height_and_width,
                    screen_height_and_width,
                ),
            ),
            (
                0,
                0,
            ),
        )
        pygame.display.update()

    def sizeCheck(
        self,
    ):
        return 800


TennisMaster()
