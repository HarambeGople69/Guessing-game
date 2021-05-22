import pygame
from pygame import mixer
import time
import random

"""INITIALIZATION OF PYGAME"""
pygame.init()

"""CREATING SCREEN"""
screen = pygame.display.set_mode((800, 600))

"""ADDING TITLE AND ICON"""
pygame.display.set_caption("Guessing Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

"""SCORE"""
sfont = pygame.font.Font("freesansbold.ttf", 35)
scorees = 0

"""MENU FONT"""
mfont = pygame.font.Font("freesansbold.ttf", 35)

repeat = True





def counts():
    global count
    global count_limit

    pygame.draw.rect(screen,(0,204,204),[280,500,300,50])
    coount = sfont.render("Chance left: " + str(count_limit), True, (0, 0, 255))

    screen.blit(coount, (280, 500))
    pygame.display.update()

def over():
    pygame.draw.rect(screen, (0, 204, 204), [280, 200, 300, 300])
    pygame.draw.rect(screen, (0, 204, 204), [300, 50, 300, 50])
    pygame.draw.rect(screen, (0, 204, 204), [340, 120, 300, 50])
    pygame.draw.rect(screen, (0, 204, 204), [280, 500, 300, 50])
    pygame.draw.rect(screen, (0, 204, 204), [180, 200, 475, 300])
    pygame.display.update()

    """WELCOME FONT"""
    gofont = pygame.font.Font("freesansbold.ttf", 35)
    game = gofont.render("GAME OVER", True, (102, 0, 0))
    screen.blit(game, (320, 70))

    """OVER TEXT"""
    ofont = pygame.font.Font("freesansbold.ttf", 30)

    o1 = ofont.render("Press Y to Play", True, (0, 0, 0))
    o2 = ofont.render("Press N to Quit", True, (0, 0, 0))
    screen.blit(o1, (280, 280))
    screen.blit(o2, (280, 320))

    pygame.display.update()

    qqq= True
    while qqq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    main()
                elif event.key == pygame.K_n:
                    quit()


def fail():
    global  count
    global count_limit
    count_limit = count_limit + count

    print(count_limit)

    counts()
    if count_limit>=1:
        guesss()
    if count_limit <= 0:
        print("out of guesses")
        over()

def win():
    wfont = pygame.font.Font("freesansbold.ttf", 35)
    playing = wfont.render("YOU WIN", True, (102, 0, 0))
    pygame.draw.rect(screen, (0, 204, 204), [280, 200, 300, 300])
    pygame.draw.rect(screen, (0, 204, 204), [300, 50, 300, 50])
    pygame.draw.rect(screen, (0, 204, 204), [340, 120, 300, 50])
    pygame.draw.rect(screen, (0, 204, 204), [280, 500, 300, 50])
    pygame.draw.rect(screen, (0, 204, 204), [180, 200, 480, 300])
    rfont = pygame.font.Font("freesansbold.ttf", 30)

    rtext1 = rfont.render("Press Y to Play Again", True, (0, 0, 0))
    rtext2 = rfont.render("Press N to Quit", True, (0, 0, 0))

    screen.blit(rtext1, (250, 230))
    screen.blit(rtext2, (250, 260))
    pygame.display.update()

    screen.blit(playing, (325, 70))

    pygame.display.update()
    y = True
    while y:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                y = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    main()
                if event.key == pygame.K_n:
                    quit()


def check():

    if c == gnum:
        win()
    elif c != gnum:

        fail()
    e = True
    while e:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


def ran():
    global a
    global b
    global c

    c = random.randint(10, 1000)
    a = c + 10
    b = c - 10
    print(c)
    guesss()


def guesss():
    global a
    global b
    global c
    i = True
    j = 0
    global gnum
    gnum = 0
    pygame.draw.rect(screen, (0, 204, 204), [250, 260, 50, 50])

    pygame.draw.rect(screen, (0, 204, 204), [250, 260, 400, 150])

    while i:

        """RANDOM TEXT"""
        rfont = pygame.font.Font("freesansbold.ttf", 30)
        rtext = rfont.render("The number lies bet " + str(b) + " and " + str(a), True, (0, 0, 0))
        screen.blit(rtext, (180, 200))

        pygame.display.update()

        gtext1 = rfont.render("Enter your guess: ", True, (0, 0, 0))
        screen.blit(gtext1, (250, 260))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    gnum = gnum * 10 + 1
                    j = 1
                elif event.key == pygame.K_2:
                    gnum = gnum * 10 + 2
                    j = 1
                elif event.key == pygame.K_3:
                    j = 1
                    gnum = gnum * 10 + 3
                elif event.key == pygame.K_4:
                    gnum = gnum * 10 + 4
                    j = 1
                elif event.key == pygame.K_5:
                    gnum = gnum * 10 + 5
                    j = 1
                elif event.key == pygame.K_6:
                    gnum = gnum * 10 + 6
                    j = 1
                elif event.key == pygame.K_7:
                    j = 1
                    gnum = gnum * 10 + 7
                elif event.key == pygame.K_8:
                    j = 1
                    gnum = gnum * 10 + 8
                elif event.key == pygame.K_9:
                    j = 1
                    gnum = gnum * 10 + 9
                elif event.key == pygame.K_0:
                    j = 1
                    gnum = gnum * 10 + 0
                if j == 1:
                    gtext2 = rfont.render("Enter your guess: " + str(gnum), True, (0, 0, 0))
                    screen.blit(gtext2, (250, 260))
                    pygame.display.update()
                if event.key == pygame.K_RETURN:
                    check()


def score():
    scores = sfont.render("Score: " + str(scorees), True, (0, 0, 255))
    screen.blit(scores, (340, 120))


def play():
    r = True
    global zzz
    wfont = pygame.font.Font("freesansbold.ttf", 35)
    playing = wfont.render("PLAYING", True, (102, 0, 0))
    pygame.draw.rect(screen, (0, 204, 204), [280, 200, 300, 300])
    pygame.draw.rect(screen, (0, 204, 204), [300, 50, 300, 50])
    screen.blit(playing, (325, 70))
    pygame.display.update()

    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False

        counts()
        pygame.display.update()
        ran()


def menu():
    while repeat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    play()
                elif event.key == pygame.K_n:
                    quit()


def welcome():
    """WELCOME FONT"""
    wfont = pygame.font.Font("freesansbold.ttf", 35)
    welcome = wfont.render("WELCOME", True, (102, 0, 0))
    screen.blit(welcome, (320, 70))


def main():


    """BACKGROUND COLOR"""
    screen.fill((0, 204, 204))

    """BACKGROUND MUSIC"""
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    """IMAGE"""
    image = pygame.image.load("confuse.png")

    """SIDE IMAGE"""
    screen.blit(image, (5, 5))
    screen.blit(image, (675, 5))

    """TITLE"""
    tfont = pygame.font.Font("freesansbold.ttf", 40)
    text = tfont.render("GUESSING NUMBER GAME", True, (255, 0, 0), (0, 255, 0))
    textrect = text.get_rect()
    textrect.center = (400, 25)
    screen.blit(text, textrect)

    """CREATED BY TEXT!"""
    font = pygame.font.Font("Kembara Cinta Demo.ttf", 40)
    creator = font.render("Created by: Utsav Shrestha", True, (0, 0, 0))
    screen.blit(creator, (225, 550))

    """EMOTES"""
    f1 = pygame.image.load("face1.png")
    f2 = pygame.image.load("face2.png")
    f3 = pygame.image.load("face3.png")
    f4 = pygame.image.load("face4.png")
    screen.blit(f1, (5, 150))
    screen.blit(f2, (665, 150))
    screen.blit(f3, (5, 450))
    screen.blit(f4, (665, 450))

    global count
    global count_limit
    count = -1
    count_limit = 5

    welcome()

    pygame.display.update()

    """GAME LOOP"""
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        time.sleep(2)
        x1 = mfont.render("Press Y to Play", True, (0, 0, 0))
        x2 = mfont.render("Press N to Quit", True, (0, 0, 0))
        screen.blit(x1, (280, 280))
        screen.blit(x2, (280, 320))
        pygame.display.update()
        menu()


main()
