import sys
import pygame

from settings import Settings

def run_game():
    pygame.init()
    DTsettings = Settings()
    screen = pygame.display.set_mode(
        (DTsettings.screen_width, DTsettings.screen_height))
    pygame.display.set_caption('Dizzy in Trouble')
    background = pygame.image.load('images/background.jpg')

    frame1 = pygame.image.load("images/2611/01.gif")
    frame2 = pygame.image.load("images/2611/02.gif")
    frame3 = pygame.image.load("images/2611/03.gif")
    frames = [frame1, frame2, frame3]
    n = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        n = n + 1
        if n > (len(frames)) * 10 - 1:
            n = 0
            screen.blit(frames[int(n / 10)], [0, 0])
        screen.blit(background, (0, 0))
        pill = pygame.image.load('images/2611/01.gif')
        screen.blit(pill, (0, 0))
        pygame.display.flip()
run_game()
