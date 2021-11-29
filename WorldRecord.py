import random
import time
import pygame
import RunningGame
import webbrowser
class WorldRecord:
    def __init__(
        screen,
        score,
        self=None,

    ):
        
        WorldRecord.postScore(score,screen)
        WorldRecord.runLink()
    def postScore(screen,score):
        print(screen)
        print(score)
        #pygame.image.save(screen, "postScores/"+"Score:"+str(screen)+".jpg")
        pygame.image.save(screen,str("postScores/currentPostedScore.jpg"))
        myfont = pygame.font.SysFont(
                "Comic Sans MS",
                20,
            )
        textsurface = myfont.render(
                "drag in your score from the postScores Folder",
                False, 
                (
                    0,
                    0,
                    0,
                ),
            )
        textsurface2 = myfont.render(
                "we will review the image and promptly add it",
                False, 
                (
                    0,
                    0,
                    0,
                ),
            )
        WorldRecord.placeBackground(screen,800)
        screen.blit(
                    textsurface,
                    (
                        10,
                        10,
                    ),
                )
        screen.blit(
                    textsurface2,
                    (
                        10,
                        50,
                    ),
                )
        pygame.display.update()
        time.sleep(0.1)

    def placeBackground(
        screen,
        screen_height_and_width,
    ):
        bg = pygame.image.load(
            "images/"
            + "whiteImage.png"
        )
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
    def runLink():
        webbrowser.open("https://docs.google.com/spreadsheets/d/1qzuQkTsrb93MiKxammCQIMiT0vmQJJoyCNlPczFkdaI/edit#gid=1150610816")
        
