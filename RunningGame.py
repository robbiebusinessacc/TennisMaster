import random
import time
import pygame

# import TennisMaster #if i have this it breaks
from Menu import *
from WorldRecord import *

class RunningGame:
    def __init__(
        self,
        direction,
        screen,
        screen_height_and_width,
        score,
        map,
        powerUps,
    ):
        self.direction = direction
        self.screen = screen
        self.screen_height_and_width = screen_height_and_width
        self.score = score
        self.map = map
        self.powerUps = powerUps
    def extraLifeInstance(screen,screen_height_and_width,score,map,powerUps,level):
        powerUps = ""
        RunningGame.lost_a_life(
            screen
        )
        print(
            "extra life over"
        )
        backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
        return(powerUps)
    def placeBackground(clear,bg,screen_height_and_width,screen,level):
        screen.blit(
            pygame.transform.scale(
                clear,
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
        working = False
        return(working)
    def processForNewBall(
            screen,
            screen_height_and_width,
            score,
            map,
            powerUps,
            level):
        backwards = True
        RunningGame.scoreBoard(
            screen,
            screen_height_and_width,
            score,
        )
        RunningGame.NextBall(
            screen,
            screen_height_and_width,
            score,
            map,
            powerUps,
            level
        )
        return(backwards)
    def ballMovement(screen,screen_height_and_width,clear,bg,ball,bomb,x,y,score,level,seperation,direction):
        

        RunningGame.placeBackground(clear,bg,screen_height_and_width,screen,level)
        screen.blit(
            pygame.transform.scale(
                ball,
                (
                    int(
                        screen_height_and_width
                        / 10
                    ),
                    int(
                        screen_height_and_width
                        / 10
                    ),
                ),
            ),
            (
                x
                - 40,
                y
                - 40,
            ),
        )
        #if direction=="right" or direction=="down":
        #    seperation=seperation*-1
        if seperation%2==0:
            y-=800
            x-=800
            y=abs(y)
            x=abs(x)
        if level==2: 
            if x==400:

                screen.blit(
                pygame.transform.scale(
                    bomb,
                    (
                        int(
                            screen_height_and_width
                            / 10
                            +20
                        ),
                        int(
                            screen_height_and_width
                            / 10
                            
                        ),
                    ),
                ),
                (
                    y
                    - 40
                    - seperation,
                    x
                    - 40
                    ,
                ),
                )
            else:
                screen.blit(
                pygame.transform.scale(
                    bomb,
                    (
                        int(
                            screen_height_and_width
                            / 10
                            +20
                        ),
                        int(
                            screen_height_and_width
                            / 10
                            
                        ),
                    ),
                ),
                (
                    y
                    - 40
                    ,
                    x
                    - 40 - seperation
                    ,
                ),
                )
        RunningGame.scoreBoard(
            screen,
            screen_height_and_width,
            score,
        )
        if seperation%2:
            temp = x
            x = y
            y = temp
        pygame.display.update()
        time.sleep(
            0.005
        )
        



    def imagesDirectory():
        return "images/"
    def tennisBall(
        direction,
        screen,
        screen_height_and_width,
        score,
        map,
        powerUps,
        level
    ):
        backwards = False
        working = True
        slowdown = 0
        speed = (
            12
            - slowdown
            + score
            * 0.5
        )
        speed = int(
            speed
        )
        ball = pygame.image.load(
            RunningGame.imagesDirectory()
            + map
            + "ball.png"
        )
        clear = pygame.image.load(
            RunningGame.imagesDirectory()
            + "whiteImage.png"
        )
        bomb = pygame.image.load(
            RunningGame.imagesDirectory()
            + "bomb.png"
        )
        if (
            powerUps
            == "scoreBoost"
            and speed
            % 4
            == 0
        ):
            score += 1
        elif (
            powerUps
            == "ballSlow"
        ):
            slowdown = 2
        score += 1
        if (
            powerUps
            == "biggerHitbox"
        ):
            biggerHitbox = True
        else:
            biggerHitbox = False
        if (
            direction
            == "left"
        ):
            x = int(
                screen_height_and_width
                / 160
            )
            y = int(
                screen_height_and_width
                / 2
            )

            bg = pygame.image.load(
                RunningGame.imagesDirectory()
                + str(
                    map
                )
                + "-left.png"
            )
            seperation=random.randint(90,155)
            while working:
                
                RunningGame.ballMovement(screen,screen_height_and_width,clear,bg,ball,bomb,x,y,score,level,seperation,direction)
                #RunningGame.ballMovement(screen,screen_height_and_width,clear,bg,ball,y,x,score,level) 
                '''if level>1:
                    RunningGame.NextBall(
                    screen,
                    screen_height_and_width,
                    score,
                    map,
                    powerUps,
                    level)'''

                x += speed

                for event in (
                    pygame.event.get()
                ):
                    if (
                        event.type
                        == pygame.KEYDOWN
                    ):
                        if (
                            event.key
                            == pygame.K_a
                            or event.key
                            == 1073741904
                        ):  # 97 = a
                            if (
                                x
                                > 200
                                and x
                                < 400
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                powerUps
                                == "extraLife"
                            ):
                                powerUps=RunningGame.extraLifeInstance(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                biggerHitbox
                                and x
                                > 150
                                and x
                                < 450
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            else:
                                RunningGame.failInstance(screen,screen_height_and_width,score)
                        else:
                            RunningGame.failInstance(screen,screen_height_and_width,score)
                    elif (
                        event.type
                        == pygame.QUIT
                    ):
                        pygame.quit()
                        exit()
                    if (
                        x
                        < screen_height_and_width
                        / 160
                    ):
                        working=RunningGame.placeBackground(clear,bg,screen_height_and_width,screen)
                    if backwards:
                        speed=RunningGame.backwardsSpeedAffect(speed)
        if (
            direction
            == "right"
        ):
            x = int(
                screen_height_and_width
            )
            y = int(
                screen_height_and_width
                / 2
            )

            bg = pygame.image.load(
                RunningGame.imagesDirectory()
                + str(
                    map
                )
                + "-right.png"
                )
            seperation=random.randint(90,155)
            while working:
                RunningGame.ballMovement(screen,screen_height_and_width,clear,bg,ball,bomb,x,y,score,level,seperation,direction)
                #RunningGame.ballMovement(screen,screen_height_and_width,clear,bg,ball,y,x,score,level)
                x -= speed
                '''if level>1:
                    RunningGame.NextBall(
                    screen,
                    screen_height_and_width,
                    score,
                    map,
                    powerUps,
                    level)'''
                for event in (
                    pygame.event.get()
                ):
                    if (
                        event.type
                        == pygame.KEYDOWN
                    ):
                        if (
                            event.key
                            == 100
                            or event.key
                            == 1073741903
                        ):  # 100 = d
                            if (
                                x
                                < 600
                                and x
                                > 400
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                powerUps
                                == "extraLife"
                            ):
                                powerUps=RunningGame.extraLifeInstance(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                biggerHitbox
                                and x
                                < 650
                                and x
                                < 350
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            else:
                                RunningGame.failInstance(screen,screen_height_and_width,score)
                        else:
                            RunningGame.failInstance(screen,screen_height_and_width,score)
                    elif (
                        event.type
                        == pygame.QUIT
                    ):
                        pygame.quit()
                        exit()
                    if (
                        x
                        < screen_height_and_width
                        / 160
                    ):
                        working=RunningGame.placeBackground(clear,bg,screen_height_and_width,screen)
                    if backwards:
                        speed=RunningGame.backwardsSpeedAffect(speed)
        if (
            direction
            == "up"
        ):
            x = int(
                screen_height_and_width
                / 2
            )
            y = int(
                int(
                    screen_height_and_width
                    / 80
                )
            )

            bg = pygame.image.load(
                RunningGame.imagesDirectory()
                + str(
                    map
                )
                + "-up.png"
            )
            seperation=random.randint(90,155)
            while working:
                RunningGame.ballMovement(screen,screen_height_and_width,clear,bg,ball,bomb,x,y,score,level,seperation,direction)
                
                y += speed
                '''if level>1:
                    RunningGame.NextBall(
                    screen,
                    screen_height_and_width,
                    score,
                    map,
                    powerUps,
                    level)'''
                for event in (
                    pygame.event.get()
                ):
                    if (
                        event.type
                        == pygame.KEYDOWN
                    ):
                        if (
                            event.key
                            == 119
                            or event.key
                            == 1073741906
                        ):  # 199 = w
                            if (
                                y
                                > 200
                                and y
                                < 400
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                powerUps
                                == "extraLife"
                            ):
                                powerUps=RunningGame.extraLifeInstance(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                biggerHitbox
                                and y
                                > 150
                                and y
                                < 450
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            else:
                                RunningGame.failInstance(screen,screen_height_and_width,score)
                        else:
                            RunningGame.failInstance(screen,screen_height_and_width,score)
                    elif (
                        event.type
                        == pygame.QUIT
                    ):
                        pygame.quit()
                        exit()
                    if (
                        x
                        < screen_height_and_width
                        / 160
                    ):
                        working=RunningGame.placeBackground(clear,bg,screen_height_and_width,screen)
                    if backwards:
                        speed=RunningGame.backwardsSpeedAffect(speed)
        if (
            direction
            == "down"
        ):
            x = int(
                screen_height_and_width
                / 2
            )
            y = int(
                int(
                    screen_height_and_width
                )
            )

            bg = pygame.image.load(
                RunningGame.imagesDirectory()
                + str(
                    map
                )
                + "-down.png"
            )
            seperation=random.randint(90,155)
            while working:
                RunningGame.ballMovement(screen,screen_height_and_width,clear,bg,ball,bomb,x,y,score,level,seperation,direction)
                #RunningGame.ballMovement(screen,screen_height_and_width,clear,bg,ball,y,x,score,level)               
                y -= speed
                '''if level>1:
                    RunningGame.NextBall(
                    screen,
                    screen_height_and_width,
                    score,
                    map,
                    powerUps,
                    level)'''
                for event in (
                    pygame.event.get()
                ):
                    if (
                        event.type
                        == pygame.KEYDOWN
                    ):
                        if (
                            event.key
                            == 115
                            or event.key
                            == 1073741905
                        ):  # 115 = a
                            if (
                                y
                                < 600
                                and y
                                > 400
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                powerUps
                                == "extraLife"
                            ):
                                powerUps=RunningGame.extraLifeInstance(screen,screen_height_and_width,score,map,powerUps,level)
                            elif (
                                biggerHitbox
                                and y
                                < 650
                                and y
                                > 350
                            ):
                                backwards = RunningGame.processForNewBall(screen,screen_height_and_width,score,map,powerUps,level)
                            else:
                                RunningGame.failInstance(screen,screen_height_and_width,score)
                        else:
                            RunningGame.failInstance(screen,screen_height_and_width,score)
                    elif (
                        event.type
                        == pygame.QUIT
                    ):
                        pygame.quit()
                        exit()
                    if (
                        x
                        < screen_height_and_width
                        / 160
                    ):
                        working=RunningGame.placeBackground(clear,bg,screen_height_and_width,screen)
                    if backwards:
                        speed=RunningGame.backwardsSpeedAffect(speed)
    def backwardsSpeedAffect(speed):
        if (
            speed
            > 0
        ):
            speed = (
                (
                    speed
                    * -1
                )
                * 2
            )
        return(speed)
    def failInstance(screen,screen_height_and_width,score):
        RunningGame.lost_a_life(
            screen
        )
        RunningGame.failScreen(
            screen,
            screen_height_and_width,
            score,
        )
        time.sleep(0.1)
    def lost_a_life(
        screen,
    ):

        clear = pygame.image.load(
            RunningGame.imagesDirectory()
            + "whiteImage.png"
        )

        lost_a_life = pygame.image.load(
            RunningGame.imagesDirectory()
            + "lostalife.png"
        )

        screen.blit(
            pygame.transform.scale(
                lost_a_life,
                (
                    300,
                    290,
                ),
            ),
            (
                250,
                255,
            ),
        )

        pygame.display.update()
        time.sleep(
            0.55
        )

    def NextBall(
        screen,
        screen_height_and_width,
        score,
        map,
        powerUps,
        level
    ):
        newDirection = random.randint(
            1,
            4,
        )
        if (
            powerUps
            == "directionHint"
        ):
            if (
                newDirection
                == 1
            ):
                x = int(
                    screen_height_and_width-screen_height_and_width+40
                )
                y = int(
                    screen_height_and_width
                    / 2
                )
                arrow = pygame.image.load(
                    RunningGame.imagesDirectory()
                    + "leftArrow.png"
                )

            if (
                newDirection
                == 2
            ):
                x = int(
                    screen_height_and_width-40
                )
                y = int(
                    screen_height_and_width
                    / 2
                )
                arrow = pygame.image.load(
                    RunningGame.imagesDirectory()
                    + "rightArrow.png"
                )
            if (
                newDirection
                == 3
            ):
                x = int(
                    screen_height_and_width
                    / 2
                )
                y = int(
                    screen_height_and_width-screen_height_and_width
                    +40
                )
                
                arrow = pygame.image.load(
                    RunningGame.imagesDirectory()
                    + "upArrow.png"
                )
            if (
                newDirection
                == 4
            ):
                x = int(
                    screen_height_and_width
                    / 2
                )
                y = int(
                    screen_height_and_width
                    -40
                )
                arrow = pygame.image.load(
                    RunningGame.imagesDirectory()
                    + "downArrow.png"
                )
                pygame.display.update()
            screen.blit(
                pygame.transform.scale(
                    arrow,
                    (
                        int(
                            screen_height_and_width
                            / 10
                        ),
                        int(
                            screen_height_and_width
                            / 10
                        ),
                    ),
                ),
                (
                    x-40,
                    y-40,
                ),
            )
            pygame.display.update()
            time.sleep(
                0.27
            )
        if (
            newDirection
            == 1
        ):
            RunningGame.tennisBall(
                "left",
                screen,
                screen_height_and_width,
                score,
                map,
                powerUps,
                level
            )
        elif (
            newDirection
            == 2
        ):
            RunningGame.tennisBall(
                "right",
                screen,
                screen_height_and_width,
                score,
                map,
                powerUps,
                level
            )
        elif (
            newDirection
            == 3
        ):
            RunningGame.tennisBall(
                "up",
                screen,
                screen_height_and_width,
                score,
                map,
                powerUps,
                level
            )
        elif (
            newDirection
            == 4
        ):
            RunningGame.tennisBall(
                "down",
                screen,
                screen_height_and_width,
                score,
                map,
                powerUps,
                level
            )

    def Convert_To_List(
        scoreText,
    ):
        newList = (
            []
        )
        eachScore = ""
        for letter in list(
            scoreText
        ):
            if (
                letter
                == ","
            ):
                if (
                    eachScore
                    != ""
                ):
                    newList.append(
                        int(
                            eachScore
                        )
                    )
                eachScore = ""
            else:
                eachScore = (
                    eachScore
                    + str(
                        int(
                            letter
                        )
                    )
                )
        return newList

    def scoreBoard(
        screen,
        screen_height_and_width,
        score,
    ):
        if (
            score
            > 100000000000000000000000000000000000000000000
        ):
            score -= 100000000000000000000000000000000000000000000
            myfont = pygame.font.SysFont(
                "Comic Sans MS",
                100,
            )
            bigfont = pygame.font.SysFont(
                "They definitely dont have this installed Gothic",
                120,
            )
            textsurface = myfont.render(
                str(
                    score
                ),
                False,
                (
                    0,
                    0,
                    0,
                ),
            )
            if (
                score
                >= 10
            ):
                screen.blit(
                    textsurface,
                    (
                        145,
                        270,
                    ),
                )
            else:
                screen.blit(
                    textsurface,
                    (
                        179,
                        270,
                    ),
                )
            with open(
                "score.txt",
                "r",
            ) as scoreFile:
                scoreText = (
                    scoreFile.read()
                )
                highScore = max(
                    RunningGame.Convert_To_List(
                        scoreText
                    )
                )
                textsurface = myfont.render(
                    ""
                    + str(
                        highScore
                    ),
                    False,
                    (
                        0,
                        0,
                        0,
                    ),
                )
                if (
                    highScore
                    >= 10
                ):
                    screen.blit(
                        textsurface,
                        (
                            541,
                            270,
                        ),
                    )
                else:
                    screen.blit(
                        textsurface,
                        (
                            570,
                            270,
                        ),
                    )
                if (
                    highScore
                    < score
                ):
                    textsurface = bigfont.render(
                        "New Highscore",
                        False,
                        (
                            0,
                            0,
                            0,
                        ),
                    )
                    screen.blit(
                        pygame.transform.scale(
                            textsurface,
                            (
                                600,
                                110,
                            ),
                        ),
                        (
                            100,
                            415,
                        ),
                    )
        else:
            myfont = pygame.font.SysFont(
                "Comic Sans MS",
                50,
            )
            textsurface = myfont.render(
                "Score: "
                + str(
                    score
                ),
                False,
                (
                    0,
                    0,
                    0,
                ),
            )
            if (
                score
                >= 10
            ):
                screen.blit(
                    textsurface,
                    (
                        10,
                        10,
                    ),
                )
            else:
                screen.blit(
                    textsurface,
                    (
                        10,
                        10,
                    ),
                )
        pygame.display.update()

    def clearBackground(
        screen,
        screen_height_and_width,
    ):
        bg = pygame.image.load(
            RunningGame.imagesDirectory()
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

    def failScreen(
        screen,
        screen_height_and_width,
        score,
    ):
        score += 100000000000000000000000000000000000000000000
        failPanel = pygame.image.load(
            RunningGame.imagesDirectory()
            + "failScreen.png"
        )
        screen.blit(
            pygame.transform.scale(
                failPanel,
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

        with open(
            "score.txt",
            "a",
        ) as scoreFile:
            scoreFile.write(
                ","
                + str(
                    score
                    - 100000000000000000000000000000000000000000000
                )
            )
        RunningGame.scoreBoard(
            screen,
            screen_height_and_width,
            score,
        )
        pygame.display.update()
        running=True
        startTime=time.time()
        while running: 
            for event in (
                pygame.event.get()
            ):
                if (event.type
                        == pygame.MOUSEBUTTONDOWN 
                        and 
                        Menu.KeyDownFunction(
                            "PostScore",
                            0,
                        )
                        ==
                        True
                    ):
                        #print(int(score)- 100000000000000000000000000000000000000000000,"<-score")
                        #print(screen,"<-screen")
                        print(screen,int(score)-100000000000000000000000000000000000000000000)
                        WorldRecord(screen,int(score)-100000000000000000000000000000000000000000000)

                elif int(time.time())-int(startTime)>5.9:

                    print("time done")
                    running=False
                if (
                    event.type
                    == pygame.KEYDOWN
                ):
                    if event.key==pygame.K_p:
                        running=False
                        print('skipped')




        # rerunning the game -------------------------
        Menu.startAnimation(
            screen,
            screen_height_and_width,
        )

        RunningGame.clearBackground(
            screen,
            screen_height_and_width,
        )
        level =  int(Menu.levelsSelection(
            screen,
            screen_height_and_width,
        ))
        map = Menu.mapSelection(
            screen,
            screen_height_and_width,
        )
        bg = pygame.image.load(
            "images/"
            + str(
                map
            )
            + ".png"
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

    def totalScores(
        scoreFile,
    ):
        totalScoreNumber = 0
        for number in scoreFile:
            if (
                number
                != 1
            ):
                totalScoreNumber += number
        return totalScoreNumber

    def sizeCheck(
        self,
    ):
        """
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
        """
        return 800
