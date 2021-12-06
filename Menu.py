import random
import time
import pygame
from Hitbox import Hitbox
class Menu:
    def __init__(
        screen,
        screen_height_and_width,
        self=None,
    ):
        self.screen = screen
        self.screen_height_and_width = screen_height_and_width
        # "images/" = "images/"
    def levelsSelection(screen,screen_height_and_width):
        with open(
            "score.txt",
            "r",
        ) as scoreFile:
            scoreText = (
                scoreFile.read()
            )
        highScore = max(
            Menu.Convert_To_List(
                scoreText
            )
        )
        clear = pygame.image.load(
            "images/"
            + "whiteImage.png"
        )

        if (
            highScore
            < 10
        ):
            LevelSelectionBG = pygame.image.load(
                "images/"
                + "level-1.png"
            )
        elif (
            highScore
            < 20
        ):
            LevelSelectionBG = pygame.image.load(
                "images/"
                + "level-2.png"
            )
        elif (
            highScore
            < 30
        ):
            LevelSelectionBG = pygame.image.load(
                "images/"
                + "level-3.png"
            )
        elif (
            highScore
            < 40
        ):
            LevelSelectionBG = pygame.image.load(
                "images/"
                + "level-4.png"
            )
        else:
            LevelSelectionBG = pygame.image.load(
                "images/"
                + "level-5.png"
            )
        screen.blit(
            pygame.transform.scale(
                LevelSelectionBG,
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
        working = True
        while working:
            for event in (
                pygame.event.get()
            ):
                if (
                    event.type
                    == pygame.KEYDOWN
                ):
                    if (
                        event.key
                        == 49
                    ):  # 49 for 1
                        return 1
                    elif (
                        event.key
                        == 50
                        and highScore
                        >= 20
                    ):  # 50 for 2
                        return 2
                    elif (
                        event.key
                        == 51
                        and highScore
                        >= 30
                    ):  # 51 for 3
                        return 3
                    elif (
                        event.key
                        == 52
                        and highScore
                        >= 40
                    ):  # 51 for 4
                        return 4
                    elif (
                        event.key
                        == 53
                        and highScore
                        >= 50
                    ):  # 51 for 5
                        return 5
                    else:
                        print(
                            "fail"
                        )
                elif (
                    event.type
                    == pygame.QUIT
                ):
                    pygame.quit()
                    exit()
                elif (
                    event.type
                    == pygame.MOUSEBUTTONDOWN 
                    and 
                    Menu.KeyDownFunction(
                        "LevelUpSelection",
                        highScore,
                    )
                    !=
                    None

                ):
                    return Menu.KeyDownFunction(
                        "LevelUpSelection",
                        highScore,
                    )

    def powerUpSelection(
        screen,
        screen_height_and_width,
    ):
        # screen = self.screen_height_and_width
        # screen_height_and_width = self.screen_height_and_width
        with open(
            "score.txt",
            "r",
        ) as scoreFile:
            scoreText = (
                scoreFile.read()
            )
        highScore = max(
            Menu.Convert_To_List(
                scoreText
            )
        )
        clear = pygame.image.load(
            "images/"
            + "whiteImage.png"
        )
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
        if (
            highScore
            < 15
        ):
            powerUpSelection = pygame.image.load(
                "images/"
                + "powerUp-1.png"
            )
        elif (
            highScore
            < 25
            and highScore
            >= 15
        ):
            powerUpSelection = pygame.image.load(
                "images/"
                + "powerUp-2.png"
            )
        elif (
            highScore
            < 35
            and highScore
            >= 25
        ):
            powerUpSelection = pygame.image.load(
                "images/"
                + "powerUp-3.png"
            )
        elif (
            highScore
            < 50
            and highScore
            >= 35
        ):
            powerUpSelection = pygame.image.load(
                "images/"
                + "powerUp-4.png"
            )
        elif (
            highScore
            >= 50
            or highScore
            == 50
        ):
            powerUpSelection = pygame.image.load(
                "images/"
                + "powerUp-5.png"
            )
        screen.blit(
            pygame.transform.scale(
                powerUpSelection,
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
        working = True
        while working:
            for event in (
                pygame.event.get()
            ):
                if (
                    event.type
                    == pygame.KEYDOWN
                ):
                    if (
                        event.key
                        == 49
                    ):  # 49 for 1
                        print(
                            "\n\nscoreBoost\n\n"
                        )
                        return "scoreBoost"
                    elif (
                        event.key
                        == 50
                        and highScore
                        >= 15
                    ):  # 50 for 2
                        print(
                            "\n\nbiggerHitbox\n\n"
                        )
                        return "biggerHitbox"
                    elif (
                        event.key
                        == 51
                        and highScore
                        >= 25
                    ):  # 51 for 3
                        print(
                            "\n\nballSlow\n\n"
                        )
                        return "ballSlow"
                    elif (
                        event.key
                        == 52
                        and highScore
                        >= 35
                    ):  # 51 for 4
                        print(
                            "\n\ndirectionHint\n\n\n\n"
                        )
                        return "directionHint"
                    elif (
                        event.key
                        == 53
                        and highScore
                        >= 50
                    ):  # 51 for 5
                        print(
                            "\n\nextraLife\n\n"
                        )
                        return "extraLife"
                    else:
                        print(
                            "fail"
                        )
                elif (
                    event.type
                    == pygame.QUIT
                ):
                    pygame.quit()
                    exit()
                elif (
                    event.type
                    == pygame.MOUSEBUTTONDOWN 
                    and 
                    Menu.KeyDownFunction(
                        "PowerUpSelection",
                        highScore,
                    )
                    !=
                    None

                ):
                    return Menu.KeyDownFunction(
                        "PowerUpSelection",
                        highScore,
                    )
        # bigger hitbox
        # slow down
        # extra life
        # score boost   every 5 balls you gain an extra point
        # direction hint
        # if you get a highscore of 75 you have an option to level up a power boost

    def KeyDownFunction(
        for_what,
        scoreThing,
    ):
        mouse = (
            pygame.mouse.get_pos()
        )
        mouseX = mouse[
            0
        ]
        mouseY = mouse[
            1
        ]

        if (
            for_what
            == "MapSelection"
        ):

            return(Menu.MapMouse(scoreThing,mouseX,mouseY))
        elif (
            for_what
            == "PowerUpSelection"
        ):
            return(Menu.PowerUpMouse(scoreThing,mouseX,mouseY))
        elif (
            for_what
            == "PostScore"
        ):
            return(Menu.postScoreMouse(scoreThing,mouseX,mouseY))
        elif (for_what=="LevelUpSelection"):
            return(Menu.LevelUpMouse(scoreThing,mouseX,mouseY))

    def postScoreMouse(scoreThing,mouseX,mouseY):
        totalScore = scoreThing
        
        if (Hitbox.isCollide(420,800,538,730,mouseX,mouseY)==True):
            return(True)
        else:
            return(False)
        
        '''
        if (
            mouseX
            > 420
            and mouseX
            < 800
            and mouseY
            > 538
            and mouseY
            < 730
        ):
            return True
        '''
    def MapMouse(scoreThing,mouseX,mouseY):
        totalScore = scoreThing

        if (
            Hitbox.isCollide(50,300,250,500,mouseX,mouseY)
        ):
            print(
                "test map 1"
            )
            return "map1"
        elif (
            Hitbox.isCollide(300,500,250,500,mouseX,mouseY)
            and totalScore
            >= 250
        ):
            print(
                "test map 2"
            )
            return "map2"
        elif (
            Hitbox.isCollide(530,750,250,500,mouseX,mouseY)
            and totalScore
            >= 500
        ):
            print(
                "test map 3"
            )
            return "map3"
    def PowerUpMouse(scoreThing,mouseX,mouseY):
        highScore = scoreThing
        if (
            Hitbox.isCollide(140,380,175,415,mouseX,mouseY)
        ):
            print(
                "\n\nscoreBoost\n\n"
            )
            return "scoreBoost"
        elif (
            Hitbox.isCollide(429,650,175,415,mouseX,mouseY)
            and highScore
            >= 15
        ):
            print(
                "\n\nbiggerHitbox\n\n"
            )
            return "biggerHitbox"
        elif (
            Hitbox.isCollide(40,260,455,690,mouseX,mouseY)
            and highScore
            >= 25
        ):
            print(
                "\n\nballSlow\n\n"
            )
            return "ballSlow"
        elif (
            Hitbox.isCollide(275,510,455,690,mouseX,mouseY)
            and highScore
            >= 35
        ):
            print(
                "\n\ndirectionHint\n\n\n\n"
            )
            return "directionHint"
        elif (
            Hitbox.isCollide(530,765,455,690,mouseX,mouseY)
            and highScore
            >= 50
        ):
            print(
                "\n\nextraLife\n\n"
            )
            return "extraLife"
    def LevelUpMouse(scoreThing,mouseX,mouseY):
        converter=Menu.PowerUpMouse(scoreThing,mouseX,mouseY)
        if converter=="scoreBoost":
            return(1)
        elif converter=="biggerHitbox":
            return(2)
        elif converter=="ballSlow":
            return(3)
        elif converter=="directionHint":
            return(4)
        elif converter=="extraLife":
            return(5)
        else:
            print("dfvuch ",converter)

    def mapSelection(
        screen,
        screen_height_and_width,
    ):
        # screen = self.screen
        # screen_height_and_width = self.screen_height_and_width
        with open(
            "score.txt",
            "r",
        ) as scoreFile:
            scoreText = (
                scoreFile.read()
            )
        totalScore = int(
            Menu.totalScores(
                Menu.Convert_To_List(
                    scoreText
                )
            )
        )
        clear = pygame.image.load(
            "images/"
            + "whiteImage.png"
        )
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
        if (
            totalScore
            < 250
        ):
            mapSelectionBG = pygame.image.load(
                "images/"
                + "mapselection-1.png"
            )
        elif (
            totalScore
            < 500
        ):
            mapSelectionBG = pygame.image.load(
                "images/"
                + "mapselection-2.png"
            )
        else:
            mapSelectionBG = pygame.image.load(
                "images/"
                + "mapselection-3.png"
            )
        screen.blit(
            pygame.transform.scale(
                mapSelectionBG,
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
        working = True
        while working:
            for event in (
                pygame.event.get()
            ):
                if (
                    event.type
                    == pygame.KEYDOWN
                ):
                    totalScore = int(
                        totalScore
                    )
                    print(
                        totalScore,
                        "\n",
                        event.key,
                    )
                    if (
                        event.key
                        == 49
                    ):  # 49 for 1
                        print(
                            "test map 1"
                        )
                        return "map1"
                    elif (
                        event.key
                        == 50
                        and totalScore
                        >= 250
                    ):  # 50 for 2
                        print(
                            "test map 2"
                        )
                        return "map2"
                    elif (
                        event.key
                        == 51
                        and totalScore
                        >= 500
                    ):  # 51 for 3
                        print(
                            "test map 3"
                        )
                        return "map3"
                    else:
                        print(
                            "failed"
                        )
                elif (
                    event.type
                    == pygame.QUIT
                ):
                    pygame.quit()
                    exit()
                elif (
                    event.type
                    == pygame.MOUSEBUTTONDOWN 
                    and 
                    Menu.KeyDownFunction(
                        "MapSelection",
                        totalScore,
                    )
                    !=
                    None

                ):
                    return Menu.KeyDownFunction(
                        "MapSelection",
                        totalScore,
                    )
        # bigger hitbox

    def Convert_To_List(
        scoreText,
    ):
        newList = (
            []
        )
        eachScore = ""
        scoreText += ","
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
            elif (
                letter
                != "\n"
            ):
                eachScore = (
                    eachScore
                    + str(
                        int(
                            letter
                        )
                    )
                )
        return newList

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

    def startAnimation(
        screen,
        screen_height_and_width,
    ):
        # screen = self.screen
        # screen_height_and_width = self.screen_height_and_width
        bg = pygame.image.load(
            "images/"
            + "startAnimation.png"
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
        working = 0
        pygame.display.update()
        while (
            working
            == 0
        ):
            for event in (
                pygame.event.get()
            ):

                if (
                    event.type
                    == pygame.KEYDOWN
                    or event.type
                    == pygame.MOUSEBUTTONDOWN
                ):
                    print(
                        "key hit"
                    )
                    working = 1
                elif (
                    event.type
                    == pygame.QUIT
                ):
                    pygame.quit()
                    exit()
